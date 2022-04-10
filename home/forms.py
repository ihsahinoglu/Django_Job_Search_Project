from django import forms
from django.forms import TextInput, FileInput, Select

from user.models import UserProfile

CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]


class CreateResumeForm(forms.ModelForm):
    image = forms.CharField(required=False, max_length=100, label='Image :')
    birth_date = forms.CharField(required=False, max_length=30, label='Birth Date :')
    sex = forms.CharField(required=False, max_length=100, help_text='Sex ', label='Sex :')
    city = forms.CharField(required=False, max_length=100, help_text='City', label='City :')
    phone = forms.CharField(required=False, max_length=200, label='Phone :')
    email = forms.EmailField(required=False, max_length=40, help_text='email', label='email :')
    web_site = forms.CharField(required=False, max_length=100, help_text='web_site', label='web_site :')
    address = forms.CharField(required=False, max_length=200, help_text='address', label='address :')

    class Meta:
        model = UserProfile
        fields = ('image', 'birth_date', 'sex', 'city', 'phone', 'email', 'web_site', 'address',)
        widgets = {
            'image': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'birth_date': TextInput(attrs={'class': 'input', 'placeholder': 'birth_date'}),
            'sex': TextInput(attrs={'class': 'input', 'placeholder': 'sex'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'web_site': TextInput(attrs={'class': 'input', 'placeholder': 'web_site'}),
        }
