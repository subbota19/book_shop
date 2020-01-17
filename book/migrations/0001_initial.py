# Generated by Django 3.0.2 on 2020-01-17 18:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriber', '__first__'),
        ('author', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2020)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='books_image/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('total_price', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)])),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Books')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriber.Subscribers')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='BooksAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.Authors')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Books')),
            ],
            options={
                'verbose_name': 'LinkBooksAuthor',
                'verbose_name_plural': 'LinkBooksAuthor',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(through='book.BooksAuthor', to='author.Authors'),
        ),
        migrations.AddField(
            model_name='books',
            name='comment',
            field=models.ManyToManyField(through='book.Comments', to='subscriber.Subscribers'),
        ),
    ]
