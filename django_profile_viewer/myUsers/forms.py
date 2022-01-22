from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from myUsers.models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Profile
        fields = ('email', 'username', 'gender', 'first_name', 'last_name')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get("email")
            password = self.cleaned_data.get("password")

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login credentials!!')



class userUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Profile
        fields = ['email', 'username', 'image']


'''class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']'''