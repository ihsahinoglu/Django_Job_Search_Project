# Generated by Django 4.0.3 on 2022-03-23 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_slug'),
        ('company', '0002_company_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Companies',
        ),
    ]
