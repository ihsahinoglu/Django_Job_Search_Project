# Generated by Django 4.0.3 on 2022-04-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='education_level',
            field=models.CharField(choices=[('İlköğretim', 'ilköğretim'), ('Lise', 'Lise'), ('Önlisans', 'Önlisans'), ('Lisans', 'Lisans'), ('Yüksek lisans', 'Yüksek lisans'), ('Doktora', 'Doktora')], max_length=30),
        ),
    ]
