# Generated by Django 4.0.3 on 2022-04-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_userskills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='images/users/user.png', upload_to='images/users/'),
        ),
    ]