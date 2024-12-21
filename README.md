# VisiOCR

VisiOCR is a Django-based web application designed for extracting text from Pan Card and Aadhar Card documents using Optical Character Recognition (OCR) technology. The project leverages Pytesseract and OpenCV to streamline text recognition with high accuracy.
___________________________________________________________________________________

# Overview

The primary goal of VisiOCR is to simplify the process of extracting and digitizing text from official identification documents. This solution is particularly useful for automation in industries requiring frequent data entry and verification from such documents.
___________________________________________________________________________________

# Objective

1.Automate text extraction from Pan Card and Aadhar Card documents.
2.Improve data entry accuracy and reduce manual effort.
3.Provide a user-friendly web interface for uploading and processing documents.
4.Ensure high accuracy and reliability of text recognition.
___________________________________________________________________________________

# Tech Stack

Programming Language: Python
Framework: Django
Libraries: Pytesseract, OpenCV
Frontend: HTML, CSS, JavaScript
Backend: Django
Database: SQLite 
___________________________________________________________________________________

# Methodology

Document Upload: Users upload images of Pan Card or Aadhar Card.
OCR Processing: The application uses Pytesseract and OpenCV to process the uploaded images and extract text.
Data Display: The extracted text is displayed on the web interface for the user to 
view or download.
Error Handling: Implements checks for image quality and format to ensure processing accuracy.
___________________________________________________________________________________

# Features

Web-based interface for uploading documents.
Accurate text extraction using OCR.
Supports multiple formats (e.g., JPG, PNG).
Easy-to-setup environment for deployment.
Minimal user interaction required for text recognition.
___________________________________________________________________________________

# Setup and Installation

1. Clone the Repository
   ''' bash git clone https://github.com/srushti207/VisiOCR.git
   cd VisiOCR
2. Create a Virtual Environment
    python -m venv venv
    For Windows: venv\Scripts\activate
3. Install Dependencies
   pip install -r requirements.txt
4. Run the Application
    python manage.py runserver
5. Access the Application Open your web browser and go to
    http://127.0.0.1:8000.
___________________________________________________________________________________

# Usage

Navigate to the application URL in your browser.
Upload an image of a Pan Card or Aadhar Card.
Click the "Extract Text" button to process the document.
View the extracted text on the results page.
___________________________________________________________________________________

# Directory Structure

VisiOCR/
├── manage.py
├── VisiOCR/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── ...
│   ├── static/
│   │   └── ...
├── requirements.txt
└── README.md





