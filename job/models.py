from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from company.models import Company


class Job(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    company = models.ForeignKey(Company, related_name='children', on_delete=models.CASCADE)
    profession = models.CharField(max_length=30)
    description = RichTextUploadingField(blank=True)
    category = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.profession

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'slug': self.slug})
