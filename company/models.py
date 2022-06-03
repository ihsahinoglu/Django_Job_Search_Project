from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from home.other import CITY_DICT, STATUS


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    auth_person = models.CharField(max_length=50)
    city = models.CharField(max_length=50, choices=CITY_DICT)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    about_company = RichTextUploadingField(blank=True, max_length=5000)
    logo = models.ImageField(blank=True, upload_to='images/', default='images/logo.png')
    employers = models.CharField(blank=True, max_length=15)
    sector = models.CharField(blank=True, max_length=30)
    web_site = models.CharField(blank=True, max_length=40)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='get_slug', null=False, unique=True)

    def get_slug(self):
        return self.user.username

    def __str__(self):
        return self.company_name

    def get_logo(self):
        if self.logo.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.logo.url))
        else:
            return ""



    """"
    def get_slug(self):
        return reverse('company_detail', kwargs={'slug': self.slug})
    """
class CompanyPhotoGallery(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

def upload_gallery_image(instance, filename):
    return f"images/{instance.company.company_name}/gallery/{filename}"