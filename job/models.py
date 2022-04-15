from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from company.models import Company


class Job(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    JOB_TYPE = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
    )
    GENDER = (
        ('Male', 'Erkek'),
        ('Female', 'Kadın'),
    )
    CITY = (
        ('İstanbul', 'İstanbul'),
        ('Ankara', 'Ankara'),
        ('İzmir', 'İzmir'),
        ('Kocaeli', 'Kocaeli'),
        ('Bursa', 'Bursa'),
        ('Şanlıurfa', 'Şanlıurfa'),
    )
    EDUCATION_LEVEL = (
        ('ilköğretim', 'ilköğretim'),
        ('Lise', 'Lise'),
        ('Önlisans', 'Önlisans'),
        ('Lisans', 'Lisans'),
        ('Yüksek lisans', 'Yüksek lisans'),
        ('Doktora', 'Doktora'),
    )
    EXPERIENCE = (
        ('Tecrübesiz', 'Tecrübesiz'),
        ('1 yıl', '1 yıl'),
        ('2 yıl', '2 yıl'),
        ('3-5 yıl', '3-5 yıl'),
        ('5-10 yıl', '5-10 yıl'),
        ('10+ yıl', '10+ yıl'),
    )
    company = models.ForeignKey(Company, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30, choices=JOB_TYPE)
    description = RichTextUploadingField(blank=True)
    category = models.CharField(max_length=30)
    city = models.CharField(max_length=20, choices=CITY)
    education_level = models.CharField(max_length=30, choices=EDUCATION_LEVEL)
    experience = models.CharField(max_length=30, choices=EXPERIENCE)
    gender = models.CharField(max_length=30, choices=GENDER)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'slug': self.slug})
