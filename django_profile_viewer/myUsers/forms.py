from django import forms
from django.contrib.auth.forms import UserCreationForm
from myUsers.models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Profile
        fields = ('email', 'username', 'gender', 'first_name', 'last_name')
