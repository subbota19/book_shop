# Generated by Django 3.0.2 on 2020-01-17 18:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3)),
                ('all_buys', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)])),
                ('cache', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)])),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
    ]
