#This was custom made
#It is advisable to create apps in django in which each app has its own views
from django.http import HttpResponse
from django.shortcuts import render

def home(response):
    # return HttpResponse("Welcome Home")
    return render(response, 'home.html')

def about(response):
    #return HttpResponse("About Us")
    return render(response, 'about.html')
