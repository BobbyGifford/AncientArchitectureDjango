# Generated by Django 2.1.4 on 2019-01-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20190117_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='locations/%Y/%m/%d'),
        ),
    ]
