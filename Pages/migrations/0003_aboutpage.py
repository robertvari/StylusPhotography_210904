# Generated by Django 3.2.7 on 2021-09-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(blank=True, max_length=2000)),
            ],
        ),
    ]
