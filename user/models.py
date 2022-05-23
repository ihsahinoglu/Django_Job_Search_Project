from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

from home.other import CITY_DICT


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20, choices=CITY_DICT)
    web_site = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/', default='images/users/user.png')
    title = models.CharField(blank=True, max_length=50)
    presentation = models.CharField(blank=True, max_length=500)

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


class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    education_add_info = models.CharField(max_length=200)

    def __str__(self):
        return self.school


class UserExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    date_from = models.CharField(max_length=30)
    date_to = models.CharField(max_length=30)
    experience_add_info = models.CharField(max_length=200)

    def __str__(self):
        return self.company


class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    skill_value = models.CharField(max_length=100)

    def __str__(self):
        return self.skill
