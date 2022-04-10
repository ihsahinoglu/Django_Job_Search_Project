from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    web_site = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    image_tag.short_description = 'Image'


class CreateResumeForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'sex', 'city', 'phone', 'address', 'web_site')
