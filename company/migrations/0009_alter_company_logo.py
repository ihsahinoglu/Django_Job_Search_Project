# Generated by Django 4.0.3 on 2022-04-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_company_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='uploads/images/logo.png', upload_to='uploads/images/'),
        ),
    ]
