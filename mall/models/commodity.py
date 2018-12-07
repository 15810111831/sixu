# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from mall.models import User,Spec,Color


class Type(models.Model):
    '''商品类别表'''
    parent = models.ForeignKey('self', verbose_name='父类', null=True, blank=True)
    name = models.CharField('分类名称', max_length=50)

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
    count = models.IntegerField('总数量', default=0)
    sale = models.IntegerField('销量', default=0)
    is_active = models.BooleanField('是否上架', default=False)

    class Meta:
        verbose_name = '商品详情'
        verbose_name_plural = '商品详情'

    def __unicode__(self):
        return self.name


class CommodityImage(models.Model):
    '''商品图片表'''
    commdity = models.ForeignKey(Commodity, verbose_name='商品')
    img_path = models.ImageField('图片地址', upload_to='images/')
    is_main = models.BooleanField('是否是主图', default=False)

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'


class CommodtyComment(models.Model):
    '''商品评价表'''
    commodity = models.ForeignKey(Commodity, verbose_name='商品')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='评论人')
    comment = models.TextField('评价内容')
    approval = models.IntegerField('点赞', default=0)
    comment_time = models.DateTimeField('评论时间', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = '商品评价'
        verbose_name_plural = '商品评价'


class CommentReply(models.Model):
    '''评论回复表'''
    comment = models.ForeignKey(CommodtyComment, verbose_name='商品评论')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='回复人')
    reply = models.TextField('回复内容')
    reply_time = models.DateTimeField('回复时间', auto_now_add=True, blank=True)
    approval = models.IntegerField('点赞', default=0)

    class Meta:
        verbose_name = '评论回复'
        verbose_name_plural = '评论回复'


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
    spec = models.ForeignKey(Spec, verbose_name='商品规格', null=True, blank=True)
    color = models.ForeignKey(Color, verbose_name='颜色', null=True, blank=True)
    count = models.IntegerField('数量')

    def save(self):
        # 保存的时候将商品总数量增加
        self.commodity.count += self.count
        self.commodity.save()
        super(Stock, self).save()

    class Meta:
        verbose_name = '库存'
        verbose_name_plural = '库存'
