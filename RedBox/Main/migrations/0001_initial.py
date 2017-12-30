# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('IMDB_rating', models.FloatField(blank=True, default=0.0)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('Director', models.CharField(blank=True, max_length=100)),
                ('Actors', models.TextField(blank=True, max_length=255)),
                ('Genre', models.CharField(max_length=100)),
                ('Sub_titles', models.CharField(blank=True, max_length=200)),
                ('trailer', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Main.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]