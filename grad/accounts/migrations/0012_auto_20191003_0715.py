# Generated by Django 2.2.5 on 2019-10-03 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='accounts/user.png', upload_to='accounts/'),
        ),
    ]
