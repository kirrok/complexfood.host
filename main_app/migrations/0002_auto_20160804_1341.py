# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='price',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='product_id',
            field=models.IntegerField(default=-1),
        ),
    ]