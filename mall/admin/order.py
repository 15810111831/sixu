from __future__ import unicode_literals

from django.contrib import admin
from mall.models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order

    search_fields = ('proxy_user', 'code', 'user')
    list_display = ('code', 'addr', 'user', 'proxy_user', 'total_addition_price',
                    'total_price', 'create_start', 'status', 'user_remark')

    readonly_fields = ('create_start','code')
    fieldsets = (
        (
            None, {
            "fields": (
                'code', 'commodity', 'user', 'proxy_user', 'count'
            ),
        }),
        (
            None,{
            'fields':(
                'addr', 'total_price', 'create_start'
                ),
            }
        ),
        (
            None, {
            'fields':(
                'status', 'user_remark'
                ),
            }
        )
    )
    

admin.site.register(Order, OrderAdmin)
