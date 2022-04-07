# Generated by Django 3.2 on 2022-04-07 08:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0010_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='static/images/ribbit-logo.png', max_length=255, verbose_name='profile_pic'),
        ),
    ]
