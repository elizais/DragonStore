# Generated by Django 3.1.4 on 2020-12-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_auto_20201228_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyers',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
