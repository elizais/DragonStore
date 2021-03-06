# Generated by Django 3.1.4 on 2020-12-23 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity_stok', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MainOder',
            fields=[
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.buyers')),
            ],
        ),
        migrations.AddField(
            model_name='buyers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='dragons',
            name='quantity_stok',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='OrderDragon',
            fields=[
                ('dragon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.dragons')),
                ('amount', models.IntegerField(default=1)),
                ('mainOder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.mainoder')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFood',
            fields=[
                ('dragon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.dfood')),
                ('amount', models.FloatField(default=1.0)),
                ('mainOder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.mainoder')),
            ],
        ),
    ]
