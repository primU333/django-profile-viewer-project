from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from myUsers.models import Profile, ProfileManager
from myUsers.forms import RegistrationForm, LoginForm

def index(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('blog-main-page')

        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'blog/index.html', context)

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('blog-main-page')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = request.POST["email"]
            user_password = request.POST["password"]
            user = authenticate(email=user_email, password=user_password)
            
            if user:
                login(request, user)
                return redirect('blog-main-page')

    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'blog/login.html', context)



def logout_veiw(request):
    logout(request)
    return redirect('/')
    #return redirect('blog-logout')


@login_required
def home(request):
    return render(request, 'blog/home.html')
