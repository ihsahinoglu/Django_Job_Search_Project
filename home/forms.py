from django import forms
from django.forms import TextInput, Select, Textarea
from apply.models import Apply
from company.models import Company
from home.models import ContactMessage
from home.other import CITY, CATEGORY, GENDER_
from job.models import Job
from user.models import UserProfile
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CreateResumeForm(forms.ModelForm):
    image = forms.ImageField(required=False, max_length=100, label='Image :')
    birth_date = forms.CharField(required=False, max_length=30, label='Birth Date :')
    gender = forms.CharField(required=False, max_length=100, help_text='Gender ', label='Gender :')
    city = forms.CharField(required=False, max_length=100, help_text='City', label='City :')
    phone = forms.CharField(required=False, max_length=200, label='Phone :')
    email = forms.EmailField(required=False, max_length=40, help_text='email', label='email :')
    web_site = forms.CharField(required=False, max_length=100, help_text='web_site', label='web_site :')
    address = forms.CharField(required=False, max_length=200, help_text='address', label='address :')
    title = forms.CharField(required=False, max_length=50, help_text='başlık', label='başlık :')
    presentation = forms.CharField(required=False, max_length=500, help_text='presentation', label='presentation :')

    educationCount = forms.CharField(required=False, max_length=100, help_text='school', label='school :')
    school = forms.CharField(required=False, max_length=100, help_text='school', label='school :')
    degree = forms.CharField(required=False, max_length=100, help_text='degree', label='degree :')
    department = forms.CharField(required=False, max_length=100, help_text='department', label='department :')
    start_date = forms.CharField(required=False, max_length=30, help_text='start_date', label='start_date :')
    end_date = forms.CharField(required=False, max_length=30, help_text='end_date', label='end_date :')
    education_add_info = forms.CharField(required=False, max_length=500, help_text='education_add_info',
                                         label='education_add_info :')

    experienceCount = forms.CharField(required=False, max_length=100, help_text='school', label='school :')
    company = forms.CharField(required=False, max_length=100, help_text='company', label='company :')
    position = forms.CharField(required=False, max_length=100, help_text='position', label='position :')
    location = forms.CharField(required=False, max_length=50, help_text='location', label='location :')
    date_from = forms.CharField(required=False, max_length=30, help_text='date_from', label='date_from :')
    date_to = forms.CharField(required=False, max_length=30, help_text='date_to', label='date_to :')
    experience_add_info = forms.CharField(required=False, max_length=500, help_text='experience_add_info',
                                          label='experience_add_info :')

    skillCount = forms.CharField(required=False, max_length=100, help_text='school', label='school :')
    skill = forms.CharField(required=False, max_length=100, help_text='skill', label='skill :')
    skill_value = forms.CharField(required=False, max_length=100, help_text='skill_value', label='skill_value :')

    class Meta:
        model = UserProfile
        fields = ('image', 'birth_date', 'gender', 'city', 'phone', 'email', 'web_site', 'address', 'title',
                  'school', 'degree', 'department', 'start_date', 'end_date', 'education_add_info',
                  'company', 'position', 'location', 'date_from', 'date_to', 'experience_add_info',
                  'skill', 'skill_value', 'educationCount', 'experienceCount', 'skillCount'
                  )


class CompanyInfoForm(forms.ModelForm):
    logo = forms.ImageField(required=False, max_length=100, label='Image :')
    company_name = forms.CharField(required=False, max_length=50, label='company_name :')
    sector = forms.CharField(required=False, max_length=100, help_text='sector ', label='sector :')
    employers = forms.CharField(required=False, max_length=200, help_text='employers', label='employers :')
    city = forms.CharField(required=False, max_length=100, help_text='City', label='City :')
    phone = forms.CharField(required=False, max_length=200, label='Phone :')
    email = forms.EmailField(required=False, max_length=40, help_text='email', label='email :')
    web_site = forms.CharField(required=False, max_length=100, help_text='web_site', label='web_site :')
    address = forms.CharField(required=False, max_length=200, help_text='address', label='address :')
    about_company = forms.CharField(required=False, max_length=500, help_text='about_company', label='about_company :')

    class Meta:
        model = Company
        fields = ('logo', 'company_name', 'sector', 'employers', 'city', 'phone', 'email', 'web_site',
                  'address', 'about_company'
                  )


class PostJobForm(forms.ModelForm):
    title = forms.CharField(required=False, max_length=50, label='title :')
    job_type = forms.CharField(required=False, max_length=30, help_text='job_type ', label='job_type :')
    category = forms.CharField(required=False, max_length=50, help_text='category', label='category :')
    city = forms.CharField(required=False, max_length=100, help_text='City', label='City :')
    gender = forms.CharField(required=False, max_length=20, label='gender :')
    education_level = forms.CharField(required=False, max_length=40, help_text='CharField', label='CharField :')
    experience = forms.CharField(required=False, max_length=100, help_text='experience', label='experience :')
    description = forms.CharField(required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Job

        fields = ('title', 'job_type', 'category', 'city', 'gender', 'education_level', 'experience',
                  'description'
                  )


class JobDetailForm(forms.ModelForm):
    title = forms.CharField(required=False, max_length=50, label='title :')
    job_type = forms.CharField(required=False, max_length=30, help_text='job_type ', label='job_type :')
    category = forms.CharField(required=False, max_length=50, help_text='category', label='category :')
    city = forms.CharField(required=False, max_length=100, help_text='City', label='City :')

    class Meta:
        model = Apply
        fields = ('title', 'job_type', 'category', 'city'
                  )

        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(required=False, max_length=50)
    city = forms.CharField(required=False, max_length=50)
    category = forms.CharField(required=False, max_length=50)

    class Meta:
        model = Company
        fields = ('query', 'city', 'category')


class SortForm(forms.Form):
    sort = forms.CharField(required=False, max_length=50)

    class Meta:
        model: Job
        fields = ('sort',)


class FAQForm(forms.Form):
    query = forms.CharField(required=False, max_length=50)
    city = forms.CharField(required=False, max_length=50)
    category = forms.CharField(required=False, max_length=50)

    class Meta:
        model = Company
        fields = ('query', 'city', 'category')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=500)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class FilterForm(forms.Form):
    customRadio1 = forms.CharField(required=False, max_length=50)
    customRadio2 = forms.CharField(required=False, max_length=50)
    customRadio3 = forms.CharField(required=False, max_length=50)
    customRadio4 = forms.CharField(required=False, max_length=50)

    class Meta:
        fields = ['customRadio1', 'customRadio2', 'customRadio3', 'customRadio4']
