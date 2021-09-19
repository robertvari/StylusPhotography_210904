# Generated by Django 3.2.7 on 2021-09-19 14:36

import Gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=Gallery.models.image_dir_path),
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
