from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def login(request):
    return render(request, 'blog/login.html')

def home(request):
    return render(request, 'blog/home.html')
