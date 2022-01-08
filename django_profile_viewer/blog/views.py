from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from myUsers.models import Profile
from myUsers.forms import RegistrationForm

def index(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(account)
            return redirect('blog-main-page')

        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'blog/index.html', context)

def login(request):
    return render(request, 'blog/login.html')

def home(request):
    '''context = {
        'Info' : Profile.objects.all()
    }'''
    return render(request, 'blog/home.html')
