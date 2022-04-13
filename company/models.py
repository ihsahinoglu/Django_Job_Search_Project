from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


class Company(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    auth_person = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    about_company = RichTextUploadingField(blank=True, max_length=500)
    logo = models.ImageField(blank=True, upload_to='images/', default='images/logo.png')
    employers = models.CharField(blank=True, max_length=15)
    sector = models.CharField(blank=True, max_length=30)
    web_site = models.CharField(blank=True, max_length=40)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.company_name

    def get_logo(self):
        if self.logo.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.logo.url))
        else:
            return ""
