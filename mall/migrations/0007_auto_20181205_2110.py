# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0006_auto_20181204_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': '\u989c\u8272\u8868', 'verbose_name_plural': '\u989c\u8272\u8868'},
        ),
        migrations.AlterModelOptions(
            name='commodityspec',
            options={'verbose_name': '\u5546\u54c1\u89c4\u683c\u5173\u8054\u8868', 'verbose_name_plural': '\u5546\u54c1\u89c4\u683c\u5173\u8054\u8868'},
        ),
        migrations.AlterModelOptions(
            name='spec',
            options={'verbose_name': '\u5546\u54c1\u89c4\u683c', 'verbose_name_plural': '\u5546\u54c1\u89c4\u683c'},
        ),
        migrations.AddField(
            model_name='commodityproxy',
            name='proxy_addition_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u4ee3\u7406\u63d0\u6210'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_addition_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u63d0\u6210\u603b\u4ef7'),
        ),
        migrations.AlterField(
            model_name='commodityproxy',
            name='proxy_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u4ee3\u7406\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u603b\u4ef7'),
        ),
    ]
