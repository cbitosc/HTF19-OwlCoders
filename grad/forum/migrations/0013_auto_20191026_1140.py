# Generated by Django 2.2.5 on 2019-10-26 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20191026_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 11, 40, 2, 954568)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='forum/def.jpg', upload_to='forum/'),
        ),
    ]
