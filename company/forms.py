from django import forms
from .models import Company, CompanyPhotoGallery


class ImageForm(forms.ModelForm):
    image1 = forms.ImageField(required=False, max_length=100, label='Image :')
    image2 = forms.ImageField(required=False, max_length=100, label='Image :')
    image3 = forms.ImageField(required=False, max_length=100, label='Image :')
    image4 = forms.ImageField(required=False, max_length=100, label='Image :')
    image5 = forms.ImageField(required=False, max_length=100, label='Image :')

    class Meta:
        model = CompanyPhotoGallery
        fields = ('image1', 'image2', 'image3', 'image4', 'image5',)
