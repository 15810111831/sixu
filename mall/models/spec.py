# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Color(models.Model):
    name = models.CharField('颜色名称', max_length=16)

    class Meta:
        verbose_name = '颜色表'
        verbose_name_plural = '颜色表'


class Spec(models.Model):
    name = models.CharField('尺码名称', max_length=16)

    class Meta:
        verbose_name = '商品规格'
        verbose_name_plural = '商品规格'

    def __unicode__(self):
        return self.name
