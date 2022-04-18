# Generated by Django 4.0.3 on 2022-04-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_rename_profession_job_title_job_education_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(choices=[('İstanbul', 'İstanbul'), ('Ankara', 'Ankara'), ('İzmir', 'İzmir'), ('Kocaeli', 'Kocaeli'), ('Bursa', 'Bursa'), ('Şanlıurfa', 'Şanlıurfa')], max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='education_level',
            field=models.CharField(choices=[('ilköğretim', 'ilköğretim'), ('Lise', 'Lise'), ('Önlisans', 'Önlisans'), ('Lisans', 'Lisans'), ('Yüksek lisans', 'Yüksek lisans'), ('Doktora', 'Doktora')], max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(choices=[('Tecrübesiz', 'Tecrübesiz'), ('1 yıl', '1 yıl'), ('2 yıl', '2 yıl'), ('3-5 yıl', '3-5 yıl'), ('5-10 yıl', '5-10 yıl'), ('10+ yıl', '10+ yıl')], max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='gender',
            field=models.CharField(choices=[('Male', 'Erkek'), ('Female', 'Kadın')], max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=30),
        ),
    ]
