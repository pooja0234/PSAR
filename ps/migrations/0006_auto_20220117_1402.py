# Generated by Django 3.0.8 on 2022-01-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='p_image',
            field=models.ImageField(default='pro.jpg', upload_to='profile'),
        ),
    ]
