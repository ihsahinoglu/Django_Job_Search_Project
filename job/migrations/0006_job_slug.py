# Generated by Django 4.0.3 on 2022-03-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_company_delete_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]