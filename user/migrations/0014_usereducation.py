# Generated by Django 4.0.3 on 2022-04-11 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0013_delete_usereducation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=30)),
                ('end_date', models.CharField(max_length=30)),
                ('education_add_info', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
