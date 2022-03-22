from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Company(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    company_name = models.CharField(max_length=150)
    auth_person = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    about_company = RichTextUploadingField(blank=True)
    logo = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    def get_logo(self):
        if self.logo.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.logo.url))
        else:
            return ""
