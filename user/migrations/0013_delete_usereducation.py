# Generated by Django 4.0.3 on 2022-04-11 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_userprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserEducation',
        ),
    ]
