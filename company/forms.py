from django import forms
from .models import Company, CompanyPhotoGallery

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = CompanyPhotoGallery
        fields = ('image',)