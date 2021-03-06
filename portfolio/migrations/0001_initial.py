# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-05 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('description', tinymce.models.HTMLField()),
                ('nationality', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('secondname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
                ('role', models.CharField(max_length=255)),
                ('githublink', models.CharField(max_length=255)),
                ('weblink', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='projectlogo/')),
                ('screenshot', models.ImageField(upload_to='projectscreenshot/')),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techlogo', models.ImageField(upload_to='techlogo/')),
                ('technologies', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='portfolio.technologies'),
        ),
    ]
