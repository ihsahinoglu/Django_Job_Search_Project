# Generated by Django 4.0.3 on 2022-05-29 17:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=5000),
        ),
    ]
