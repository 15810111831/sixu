# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodityimage',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u4e3b\u56fe'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u5206\u7c7b\u540d\u79f0'),
        ),
    ]
