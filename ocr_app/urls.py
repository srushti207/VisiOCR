from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('upload/', views.upload_image, name='upload_image'),  # Upload image page
    path('generate_visitor_pass/', views.generate_visitor_pass, name='generate_visitor_pass'),  # Generate visitor pass
    path('visitor_page/', views.visitor_page, name='visitor_page'),  # Visitor information page
]
