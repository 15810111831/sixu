# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.validators import ASCIIUsernameValidator


class User(AbstractUser):
    """用户表"""
    username = models.CharField('用户名', max_length=32, 
        unique=True,
        error_messages={
            'unique':u'相同用户名已存在'
        })

    is_active = models.BooleanField("启用", default=True)
    is_staff = models.BooleanField("允许登录", default=True)
    is_admin = models.BooleanField("管理员", default=False)
    is_proxy = models.BooleanField('是否为代理人', default=False)
    date_joined = models.DateTimeField("注册时间", auto_now_add=True)
    real_name = models.CharField("姓名",max_length=30, null=True, blank=True)
    mobile = models.CharField("手机号",  unique=True,
                error_messages={'unique': u'手机号已存在'},
                max_length=30, null=True, blank=True)
    email = models.EmailField('邮箱', null=True, blank=True)

    groups = models.ManyToManyField(Group, null=True, blank=True, verbose_name='用户组')


    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

class UserOpenid(models.Model):
    """用户微信信息表"""
    user = models.ForeignKey(User, verbose_name='用户OPENID')
    openid = models.CharField('openid', max_length=50)
    appid = models.CharField('公众号ID', max_length=50)
    head_img = models.ImageField('头像', max_length=200, upload_to='user_head_images/',null=True, blank=True)
    nickname = models.CharField('昵称', max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.openid

    class Meta:
        verbose_name = '用户微信信息表'
        verbose_name_plural = '用户微信信息表'

class AddressUser(models.Model):
    '''用户地址表'''
    user = models.ForeignKey(User, verbose_name='用户')
    addr = models.CharField('地址', max_length=150)
    zip_code = models.CharField('邮编', max_length=10)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.addr

    class Meta:
        verbose_name = '地址管理'
        verbose_name_plural = '地址管理'
