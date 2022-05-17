# Generated by Django 4.0.3 on 2022-05-17 21:11

import company.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='auth_person',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(choices=[('Adana', 'Adana'), ('Adıyaman', 'Adıyaman'), ('Afyon', 'Afyon'), ('Ağrı', 'Ağrı'), ('Amasya', 'Amasya'), ('Ankara', 'Ankara'), ('Antalya', 'Antalya'), ('Artvin', 'Artvin'), ('Aydın', 'Aydın'), ('Balıkesir', 'Balıkesir'), ('Bilecik', 'Bilecik'), ('Bingöl', 'Bingöl'), ('Bitlis', 'Bitlis'), ('Bolu', 'Bolu'), ('Burdur', 'Burdur'), ('Bursa', 'Bursa'), ('Çanakkale', 'Çanakkale'), ('Çankırı', 'Çankırı'), ('Çorum', 'Çorum'), ('Denizli', 'Denizli'), ('Diyarbakır', 'Diyarbakır'), ('Edirne', 'Edirne'), ('Elazığ', 'Elazığ'), ('Erzincan', 'Erzincan'), ('Erzurum', 'Erzurum'), ('Eskişehir', 'Eskişehir'), ('Gaziantep', 'Gaziantep'), ('Giresun', 'Giresun'), ('Gümüşhane', 'Gümüşhane'), ('Hakkari', 'Hakkari'), ('Hatay', 'Hatay'), ('Isparta', 'Isparta'), ('İçel (Mersin)', 'İçel (Mersin)'), ('İstanbul', 'İstanbul'), ('İzmir', 'İzmir'), ('Kars', 'Kars'), ('Kastamonu', 'Kastamonu'), ('Kayseri', 'Kayseri'), ('Kırklareli', 'Kırklareli'), ('Kırşehir', 'Kırşehir'), ('Kocaeli', 'Kocaeli'), ('Konya', 'Konya'), ('Kütahya', 'Kütahya'), ('Malatya', 'Malatya'), ('Manisa', 'Manisa'), ('Kahramanmaraş', 'Kahramanmaraş'), ('Mardin', 'Mardin'), ('Muğla', 'Muğla'), ('Muş', 'Muş'), ('Nevşehir', 'Nevşehir'), ('Niğde', 'Niğde'), ('Ordu', 'Ordu'), ('Rize', 'Rize'), ('Sakarya', 'Sakarya'), ('Samsun', 'Samsun'), ('Siirt', 'Siirt'), ('Sinop', 'Sinop'), ('Sivas', 'Sivas'), ('Tekirdağ', 'Tekirdağ'), ('Tokat', 'Tokat'), ('Trabzon', 'Trabzon'), ('Tunceli', 'Tunceli'), ('Şanlıurfa', 'Şanlıurfa'), ('Uşak', 'Uşak'), ('Van', 'Van'), ('Yozgat', 'Yozgat'), ('Zonguldak', 'Zonguldak'), ('Aksaray', 'Aksaray'), ('Bayburt', 'Bayburt'), ('Karaman', 'Karaman'), ('Kırıkkale', 'Kırıkkale'), ('Batman', 'Batman'), ('Şırnak', 'Şırnak'), ('Bartın', 'Bartın'), ('Ardahan', 'Ardahan'), ('Iğdır', 'Iğdır'), ('Yalova', 'Yalova'), ('Karabük', 'Karabük'), ('Kilis', 'Kilis'), ('Osmaniye', 'Osmaniye'), ('Düzce', 'Düzce')], max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='CompanyPhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=company.models.upload_gallery_image)),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='company.company')),
            ],
        ),
    ]
