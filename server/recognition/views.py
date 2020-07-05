# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os , sys
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import HotelForm
from .models import Hotel
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

#Path images
IMAGE_PATH = "/home/loc/XUANLOC/PROJECT/server_django"

def index(request):
    return HttpResponse("Hello")

def display_image(request):
    list_images = []
    list_images = os.listdir(IMAGE_PATH)
  
    # if request.method == 'POST': 
    #     form = HotelForm(request.POST, request.FILES) 
  
    #     if form.is_valid(): 
    #         form.save() 
    #         return redirect('success') 
    # else: 
    #     form = HotelForm() 
    # return render(request, 'display_images.html', {'form' : form}) 
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'load_images.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'load_images.html')

# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'hotel_image_form.html', {'form' : form}) 

def success(request): 
    return HttpResponse('successfully uploaded')

def display_hotel_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render(request, 'display_images.html', {'hotel_images' : Hotels})  