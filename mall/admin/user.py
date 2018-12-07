# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mall.models import UserOpenid, AddressUser, User

class UserOpenidInlineAdmin(admin.TabularInline):
    model = UserOpenid
    fields = ('openid', 'appid', 'head_img')


class AddressUserInlineAdmin(admin.TabularInline):
    model = AddressUser
    fields = ('addr', 'zip_code')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'is_active', 'is_staff', 'is_proxy')
    exclude = ('date_joined',)
    filter_horizontal = ('groups',)

    fieldsets = (
        (
            None, {
                'fields': ('username', 'mobile', 'email')
            }
        ),
        (
            None, {
                'fields': ('real_name',)
            }
        ),
        (
            None, {
                'fields': ('is_active', 'is_staff', 'is_proxy')
            }
        )
    )

    inlines = [UserOpenidInlineAdmin, AddressUserInlineAdmin]

admin.site.site_header = '思绪万千后台管理'
admin.site.site_title = '思绪万千'
admin.site.register(User, UserAdmin)
