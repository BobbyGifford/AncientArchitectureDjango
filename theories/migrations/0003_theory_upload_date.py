# Generated by Django 2.1.4 on 2019-01-22 23:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theories', '0002_auto_20190118_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='theory',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 22, 15, 49, 56, 819014)),
        ),
    ]
