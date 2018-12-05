# coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from mall.models import Stock


class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ('commodity', 'spec', 'color', 'count')

    fields = ('commodity', 'spec', 'color', 'count')


admin.site.register(Stock, StockAdmin)
