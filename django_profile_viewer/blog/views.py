from django.shortcuts import render
from django.http import HttpResponse
from .models import Info

def index(request):
    return render(request, 'blog/index.html')

def login(request):
    return render(request, 'blog/login.html')

def home(request):
    context = {
        'Info' : Info.objects.all()
    }
    return render(request, 'blog/home.html', context)
