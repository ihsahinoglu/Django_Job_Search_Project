# Generated by Django 4.0.3 on 2022-03-22 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('job', '0004_job_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='company.company'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
