# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_commodityimage_commodtycomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='description',
            field=models.TextField(max_length=200, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='useropenid',
            name='appid',
            field=models.CharField(max_length=50, verbose_name='\u516c\u4f17\u53f7ID'),
        ),
        migrations.AlterField(
            model_name='useropenid',
            name='head_img',
            field=models.CharField(max_length=200, verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='useropenid',
            name='openid',
            field=models.CharField(max_length=50, verbose_name='openid'),
        ),
    ]
