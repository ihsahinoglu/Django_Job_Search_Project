from django import forms
from django.forms import TextInput, Select

from user.models import UserProfile

CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]


class CreateResumeForm(forms.ModelForm):
    image = forms.ImageField(required=False, max_length=100, label='Image :')
    birth_date = forms.CharField(required=False, max_length=30, label='Birth Date :')
    sex = forms.CharField(required=False, max_length=100, help_text='Sex ', label='Sex :')
    city = forms.CharField(required=False, max_length=100, help_text='City', label='City :')
    phone = forms.CharField(required=False, max_length=200, label='Phone :')
    email = forms.EmailField(required=False, max_length=40, help_text='email', label='email :')
    web_site = forms.CharField(required=False, max_length=100, help_text='web_site', label='web_site :')
    address = forms.CharField(required=False, max_length=200, help_text='address', label='address :')
    presentation = forms.CharField(required=False, max_length=500, help_text='presentation', label='presentation :')

    school = forms.CharField(required=False, max_length=100, help_text='school', label='school :')
    degree = forms.CharField(required=False, max_length=100, help_text='degree', label='degree :')
    department = forms.CharField(required=False, max_length=100, help_text='department', label='department :')
    start_date = forms.CharField(required=False, max_length=30, help_text='start_date', label='start_date :')
    end_date = forms.CharField(required=False, max_length=30, help_text='end_date', label='end_date :')
    education_add_info = forms.CharField(required=False, max_length=500, help_text='education_add_info',
                                         label='education_add_info :')

    company = forms.CharField(required=False, max_length=100, help_text='company', label='company :')
    position = forms.CharField(required=False, max_length=100, help_text='position', label='position :')
    location = forms.CharField(required=False, max_length=50, help_text='location', label='location :')
    date_from = forms.CharField(required=False, max_length=30, help_text='date_from', label='date_from :')
    date_to = forms.CharField(required=False, max_length=30, help_text='date_to', label='date_to :')
    experience_add_info = forms.CharField(required=False, max_length=500, help_text='experience_add_info',
                                          label='experience_add_info :')

    skill = forms.CharField(required=False, max_length=100, help_text='skill', label='skill :')
    skill_value = forms.CharField(required=False, max_length=100, help_text='skill_value', label='skill_value :')

    class Meta:
        model = UserProfile
        fields = ('image', 'birth_date', 'sex', 'city', 'phone', 'email', 'web_site', 'address',
                  'school', 'degree', 'department', 'start_date', 'end_date', 'education_add_info',
                  'company', 'position', 'location', 'date_from', 'date_to', 'experience_add_info',
                  'skill', 'skill_value'
                  )

        widgets = {
            'image': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'birth_date': TextInput(attrs={'class': 'input', 'placeholder': 'birth_date'}),
            'sex': TextInput(attrs={'class': 'input', 'placeholder': 'sex'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'web_site': TextInput(attrs={'class': 'input', 'placeholder': 'web_site'}),
            'presentation': TextInput(attrs={'class': 'input', 'placeholder': 'presentation'}),

            'school': TextInput(attrs={'class': 'input', 'placeholder': 'school'}),
            'degree': Select(attrs={'class': 'input', 'placeholder': 'degree'}),
            'department': TextInput(attrs={'class': 'input', 'placeholder': 'department'}),
            'start_date': TextInput(attrs={'class': 'input', 'placeholder': 'start_date'}),
            'end_date': TextInput(attrs={'class': 'input', 'placeholder': 'end_date'}),
            'education_add_info': TextInput(attrs={'class': 'input', 'placeholder': 'education_add_info'}),

            'company': TextInput(attrs={'class': 'input', 'placeholder': 'company'}),
            'position': TextInput(attrs={'class': 'input', 'placeholder': 'position'}),
            'location': Select(attrs={'class': 'input', 'placeholder': 'location'}),
            'date_from': TextInput(attrs={'class': 'input', 'placeholder': 'date_from'}),
            'date_to': TextInput(attrs={'class': 'input', 'placeholder': 'date_to'}),
            'experience_add_info': TextInput(attrs={'class': 'input', 'placeholder': 'experience_add_info'}),

            'skill': TextInput(attrs={'class': 'input', 'placeholder': 'skill'}),
            'skill_value': TextInput(attrs={'class': 'input', 'placeholder': 'skill_value'}),

        }
