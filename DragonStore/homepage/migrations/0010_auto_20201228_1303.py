# Generated by Django 3.1.4 on 2020-12-28 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20201228_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyers',
            name='dragon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.dragons'),
        ),
    ]
