from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name :')
    email = forms.EmailField(max_length=200, label='Email :')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CompanySignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name :')
    company_name = forms.CharField(max_length=100, help_text='Company Name', label='Company Name :')
    email = forms.EmailField(max_length=200, label='Email :')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'company_name', 'email', 'password1', 'password2',)


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=200, label='Email :')

    class Meta:
        model = User
        fields = ('email',)

