# Generated by Django 3.1.4 on 2020-12-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20201227_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='dragons',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dragons'),
        ),
    ]
