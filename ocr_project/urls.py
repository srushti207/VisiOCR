from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ocr_app.urls')),  # Replace 'ocr_app' with your app's name
]
