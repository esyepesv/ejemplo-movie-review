from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome Stiven to Home Page</h1>')

