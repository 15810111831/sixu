# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import decimal
from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
from mall.models import AddressUser
from mall.models import Commodity, Spec, Color, Stock


class Order(models.Model):
    """订单表"""
    commodity = models.ForeignKey(Commodity, verbose_name='商品')
    spec = models.ForeignKey(Spec, verbose_name='规格')
    color = models.ForeignKey(Color, verbose_name='颜色')
    addr = models.ForeignKey(AddressUser, verbose_name='订单寄往地址')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户')
    proxy_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='代理人', 
        null=True, blank=True, related_name='proxy_user')
    code = models.CharField('订单号', max_length=16, blank=True)
    count = models.IntegerField('商品数量', default=1)
    total_price = models.DecimalField('总价', max_digits=10, decimal_places=2, blank=True, null=True)
    total_addition_price = models.DecimalField('提成总价', max_digits=10, decimal_places=2, blank=True, null=True)

    STATUS_CHOICE = (
        (0, '未支付'),
        (1, '已支付')
    )
    status = models.SmallIntegerField('订单状态', choices=STATUS_CHOICE, default=0)

    user_remark = models.CharField('顾客描述', max_length=200, null=True, blank=True)
    create_start = models.DateTimeField(
        '下单时间', auto_now_add=True, blank=True, editable=False)

    def create_code(self):
        ''' 创建订单编码，当新建订单时创建不能修改'''
        while True:
            random10 = get_random_string(10, allowed_chars='0123456789')
            code = datetime.now().strftime('%Y%m%d') + random10
            code_exists = Order.objects.filter(code=code).exists()
            if not code_exists:
                return code

        raise Exception("创建订单编码code失败")

    def get_total_price(self):
        commodity_proxy = self.commodityproxy_set.first()
        if commodity_proxy:
            return commodity_proxy.proxy_price * self.count
        return self.commodity.price * self.count

    def get_total_addition_price(self):
        commodity_proxy = self.commodityproxy_set.first()
        if commodity_proxy:
            return commodity_proxy.proxy_addition_price * self.count
        return decimal.Decimal(0.00)

    def save(self, *args, **kwargs):
        # 只创建一次code
        if self._state.adding:
            self.code = self.create_code()
            # 只有第一次的时候赋值,当修改的时候保存修改的信息
            self.total_price = self.get_total_price()
            self.total_addition_price = self.get_total_addition_price()

            # 减去下单数量
            stock = Stock.objects.get(commodity=self.commodity, spec=self.spec, color=self.color)
            stock.count -= 1
            stock.save(0)

        super(Order, self).save(*args, **kwargs)


    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = '订单表'
