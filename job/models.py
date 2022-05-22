from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

from company.models import Company
from home.other import CITY_DICT, STATUS, JOB_TYPE, EDUCATION_LEVEL, EXPERIENCE, GENDER_


class Job(models.Model):
    company = models.ForeignKey(Company, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30, choices=JOB_TYPE)
    description = RichTextUploadingField(blank=True, max_length=5000,)
    category = models.CharField(max_length=30)
    city = models.CharField(max_length=20, choices=CITY_DICT)
    education_level = models.CharField(max_length=30, choices=EDUCATION_LEVEL)
    experience = models.CharField(max_length=30, choices=EXPERIENCE)
    gender = models.CharField(max_length=30, choices=GENDER_)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = AutoSlugField(populate_from='get_slug', unique=True, null=False)

    def get_slug(self):
        return self.company.company_name + " " + self.title

    def __str__(self):
        return self.title
