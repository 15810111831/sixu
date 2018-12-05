# coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from mall.models import Spec, Color


class SpecAdmin(admin.ModelAdmin):
    model = Spec
    list_display = ('name', 'color')

    fields = ('name', 'color')

