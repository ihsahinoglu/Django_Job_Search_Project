# Generated by Django 4.0.3 on 2022-04-26 14:23

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]