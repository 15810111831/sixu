# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mall.models import Commodity, CommodityImage, CommodtyComment, CommodityProxy
from mall.models import Type

class CommodityImageInlineAdmin(admin.TabularInline):
    model = CommodityImage
    fields = ('img_path',)


class CommodityCommentInlineAdmin(admin.TabularInline):
    model = CommodtyComment
    fields = ('text', 'approval')

class CommodityProxyInlineAdmin(admin.TabularInline):
    model = CommodityProxy
    fields = ('user', 'proxy_price')

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count')
    fields = ('name','type' ,'price' ,'count' ,'description')
    inlines = [CommodityImageInlineAdmin, CommodityProxyInlineAdmin, CommodityCommentInlineAdmin]


admin.site.register(Commodity, CommodityAdmin)
admin.site.register(Type)
admin.site.register(CommodityImage)
