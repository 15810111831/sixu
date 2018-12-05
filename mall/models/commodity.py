# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mall.models import User,Spec,Color


class Type(models.Model):
    '''商品类别表'''
    parent = models.ForeignKey('self', verbose_name='父类', null=True, blank=True)
    name = models.CharField('分类', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = '商品分类'


class Commodity(models.Model):
    '''商品详情表'''
    type = models.ForeignKey(Type, verbose_name='类别')
    name = models.CharField('商品名称', max_length=50)
    price = models.DecimalField('价格',max_digits=10, decimal_places=2)
    description = models.TextField('描述', max_length=200)
    count = models.IntegerField('数量', default=1)

    class Meta:
        verbose_name = '商品详情'
        verbose_name_plural = '商品详情'

    def __unicode__(self):
        return self.name


class CommodityImage(models.Model):
    '''商品图片表'''
    commdity = models.ForeignKey(Commodity, verbose_name='商品图片')
    img_path = models.ImageField('图片地址', upload_to='images/')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'


class CommodtyComment(models.Model):
    '''商品评价表'''
    commodity = models.ForeignKey(Commodity, verbose_name='商品评价')
    text = models.TextField('评价')
    approval = models.IntegerField('点赞', default=0)

    class Meta:
        verbose_name = '商品评价'
        verbose_name_plural = '商品评价'


class CommodityProxy(models.Model):
    '''商品代理人表-不同代理人不同的代理价格'''
    user = models.ForeignKey(User, verbose_name='代理人')
    commodity = models.ForeignKey(Commodity, verbose_name='代理商品')
    proxy_price = models.DecimalField('代理价格', max_digits=10, decimal_places=2, null=True, blank=True)
    proxy_addition_price = models.DecimalField('代理提成', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = '商品代理人'
        verbose_name_plural = '商品代理人'


class Stock(models.Model):
    '''库存表'''
    commodity = models.ForeignKey(Commodity, verbose_name='商品')
    spec = models.ForeignKey(Spec, verbose_name='商品规格')
    color = models.ForeignKey(Color, verbose_name='颜色')
    count = models.IntegerField('数量')

    class Meta:
        verbose_name = '库存'
        verbose_name_plural = '库存'
