import cv2
import numpy as np
import pytesseract
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

def home(request):
    return render(request, 'ocr_app/home.html')

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return processed_image

def extract_info(image):
    processed_image = preprocess_image(image)
    text = pytesseract.image_to_string(processed_image)
    name, birth_date = parse_text(text) 
    return name, birth_date

def parse_text(text):
    name = None
    birth_date = None

    all_text_list = re.split(r'[\n]', text)
    text_list = [i.strip() for i in all_text_list if i.strip()]

    if "MALE" in text or "male" in text or "FEMALE" in text or "female" in text :
        name = aadhar_name(text_list)
    else:
        name = pan_name(text)

    dob_match_pan = re.search(r'(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
    if dob_match_pan:
        birth_date = dob_match_pan.group(0).strip() 
    return name, birth_date

def aadhar_name(text_list):
    user_name = None
    aadhar_dob_pat = r'(YoB|YOB:|DOB:|DOB|AOB)'
    date_ele = None
    for idx, i in enumerate(text_list):
        if re.search(aadhar_dob_pat, i):
            date_ele = i
            break

    if date_ele:
        user_name = text_list[idx-1]

    pattern = re.search(r'([A-Z][a-zA-Z\s]+)', user_name)
    if pattern:
        name = pattern.group(0).strip()
    else:
        name = None
    return name

def pan_name(text):
    pancard_name = None
    name_patterns = [
        r'(Name\s*\n[A-Z\s]+)',
        r'(Name\s*\n[A-Z]+[\s]+[A-Z]+[\s]+[A-Z]+[\s])',   
        r'(Name\s*\n[A-Z]+[\s]+[A-Z]+[\s])', 
    ]

    for pattern in name_patterns:
        name_match_pan = re.search(pattern, text)
        if name_match_pan:
            matched_name = name_match_pan.group(1).strip().replace('\n', ' ') 
            pancard_name = re.sub(r'^Name\s+', '', matched_name)
            break
    return pancard_name

def process_image(image):
    name, birth_date = extract_info(image)
    if name is not None:
        name = name.upper()
    if birth_date is None:
        age = None
    else:
        age = calculate_age(birth_date)
    
    return name, birth_date, age

def calculate_age(birth_date):
    try:
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        age = (datetime.now() - birth_date).days // 365
    except (ValueError, TypeError):
        birth_date = None
        age = None
    return age

@csrf_exempt 
def upload_image(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_file = request.FILES['image']
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), -1)
            name, birth_date, age = process_image(image)

            if birth_date is None or name is None:
                return render(request, 'ocr_app/home.html', {'error_message': "Image quality is too poor. Please try again or add the details manually."})
            return render(request, 'ocr_app/home.html', {'name': name, 'birth_date': birth_date, 'age': age})
        else:
            name = request.POST.get('name')
            birth_date = request.POST.get('birth_date')
            age = calculate_age(birth_date)   
            return render(request, 'ocr_app/home.html', {'name': name, 'birth_date': birth_date, 'age': age})

    return render(request, 'ocr_app/home.html')

def generate_visitor_pass(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birth_date = request.POST.get('birth_date')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if not name or not birth_date or not age or not email:
            return redirect('home')  # Ensure all fields are provided

        # Construct the URL with query parameters
        redirect_url = f'/visitor_page/?name={name}&birth_date={birth_date}&age={age}&email={email}'
        print("Redirect URL:", redirect_url)  # Debugging URL construction
        return redirect(redirect_url)


def visitor_page(request):
    # Extract parameters from URL
    name = request.GET.get('name', 'N/A')
    birth_date = request.GET.get('birth_date', 'N/A')
    age = request.GET.get('age', 'N/A')
    email = request.GET.get('email', 'N/A')

    print(f"Name: {name}, Birth Date: {birth_date}, Age: {age}, Email: {email}")  # Debugging print

    # Pass data to template
    return render(request, 'ocr_app/visitor.html', {
        'name': name,
        'birth_date': birth_date,
        'age': age,
        'email': email,
    })
