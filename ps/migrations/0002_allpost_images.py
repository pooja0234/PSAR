# Generated by Django 3.0.8 on 2022-01-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpost',
            name='images',
            field=models.ImageField(default=1, upload_to='', verbose_name=''),
            preserve_default=False,
        ),
    ]
