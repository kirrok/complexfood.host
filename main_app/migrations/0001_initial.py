# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-01 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('protein', models.CharField(blank=True, max_length=150)),
                ('carbohydrates', models.CharField(blank=True, max_length=100)),
                ('greens', models.CharField(blank=True, max_length=100)),
                ('other', models.CharField(blank=True, max_length=100)),
                ('pcal', models.IntegerField()),
                ('ccal', models.IntegerField()),
                ('gcal', models.IntegerField()),
                ('ocal', models.IntegerField()),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=20)),
                ('calories', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('carbohydrates', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('first_description_woman', models.CharField(blank=True, max_length=100)),
                ('first_description_man', models.CharField(blank=True, max_length=100)),
                ('second_description', models.TextField(blank=True, max_length=400)),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.AddField(
            model_name='ration',
            name='set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.set'),
        ),
    ]
