# Generated by Django 4.0.3 on 2022-04-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_userprofile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='sex',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='uploads/images/users/user.png', upload_to='uploads/images/users/'),
        ),
    ]
