# Generated by Django 3.0.8 on 2022-01-10 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ps', '0002_allpost_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allpost',
            name='images',
        ),
    ]
