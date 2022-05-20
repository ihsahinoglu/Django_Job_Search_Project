from django import forms
from .models import Company, CompanyPhotoGallery

class ImageForm(forms.ModelForm):
    class Meta:
        model = CompanyPhotoGallery
        fields = ('image',)