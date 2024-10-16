# Generated by Django 5.1.1 on 2024-10-08 11:06

import cloudinary.models
import django.utils.timezone
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eltonapp', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
