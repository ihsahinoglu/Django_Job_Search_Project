# Generated by Django 4.0.3 on 2022-04-23 23:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_alter_job_gender_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]