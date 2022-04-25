from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from company.models import Company
from home.other import CITY_DICT, STATUS, JOB_TYPE, EDUCATION_LEVEL, EXPERIENCE, GENDER_


class Job(models.Model):
    company = models.ForeignKey(Company, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30, choices=JOB_TYPE)
    description = RichTextUploadingField(blank=True)
    category = models.CharField(max_length=30)
    city = models.CharField(max_length=20, choices=CITY_DICT)
    education_level = models.CharField(max_length=30, choices=EDUCATION_LEVEL)
    experience = models.CharField(max_length=30, choices=EXPERIENCE)
    gender = models.CharField(max_length=30, choices=GENDER_)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'slug': self.slug})
