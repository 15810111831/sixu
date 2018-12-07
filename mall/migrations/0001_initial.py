# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 13:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('username', models.CharField(error_messages={'unique': '\u76f8\u540c\u7528\u6237\u540d\u5df2\u5b58\u5728'}, max_length=32, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u542f\u7528')),
                ('is_staff', models.BooleanField(default=True, verbose_name='\u5141\u8bb8\u767b\u5f55')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u7ba1\u7406\u5458')),
                ('is_proxy', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u4ee3\u7406\u4eba')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u6ce8\u518c\u65f6\u95f4')),
                ('real_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u59d3\u540d')),
                ('mobile', models.CharField(blank=True, error_messages={'unique': '\u624b\u673a\u53f7\u5df2\u5b58\u5728'}, max_length=30, null=True, unique=True, verbose_name='\u624b\u673a\u53f7')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('groups', models.ManyToManyField(blank=True, null=True, to='auth.Group', verbose_name='\u7528\u6237\u7ec4')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8868',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AddressUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=150, verbose_name='\u5730\u5740')),
                ('zip_code', models.CharField(max_length=10, verbose_name='\u90ae\u7f16')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u5730\u5740\u7ba1\u7406',
                'verbose_name_plural': '\u5730\u5740\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='\u989c\u8272\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u989c\u8272\u8868',
                'verbose_name_plural': '\u989c\u8272\u8868',
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='\u56de\u590d\u5185\u5bb9')),
                ('reply_time', models.DateTimeField(auto_now_add=True, verbose_name='\u56de\u590d\u65f6\u95f4')),
                ('approval', models.IntegerField(default=0, verbose_name='\u70b9\u8d5e')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba\u56de\u590d',
                'verbose_name_plural': '\u8bc4\u8bba\u56de\u590d',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u4ef7\u683c')),
                ('description', models.TextField(max_length=200, verbose_name='\u63cf\u8ff0')),
                ('count', models.IntegerField(default=0, verbose_name='\u603b\u6570\u91cf')),
                ('sale', models.IntegerField(default=0, verbose_name='\u9500\u91cf')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e0a\u67b6')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u8be6\u60c5',
                'verbose_name_plural': '\u5546\u54c1\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='CommodityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.ImageField(upload_to='images/', verbose_name='\u56fe\u7247\u5730\u5740')),
                ('commdity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Commodity', verbose_name='\u5546\u54c1\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u5546\u54c1\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='CommodityProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u4ee3\u7406\u4ef7\u683c')),
                ('proxy_addition_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u4ee3\u7406\u63d0\u6210')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Commodity', verbose_name='\u4ee3\u7406\u5546\u54c1')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4ee3\u7406\u4eba')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u4ee3\u7406\u4eba',
                'verbose_name_plural': '\u5546\u54c1\u4ee3\u7406\u4eba',
            },
        ),
        migrations.CreateModel(
            name='CommodtyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='\u8bc4\u4ef7\u5185\u5bb9')),
                ('approval', models.IntegerField(default=0, verbose_name='\u70b9\u8d5e')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Commodity', verbose_name='\u5546\u54c1\u8bc4\u4ef7')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8bc4\u8bba\u4eba')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u8bc4\u4ef7',
                'verbose_name_plural': '\u5546\u54c1\u8bc4\u4ef7',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=16, verbose_name='\u8ba2\u5355\u53f7')),
                ('count', models.IntegerField(default=1, verbose_name='\u5546\u54c1\u6570\u91cf')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u603b\u4ef7')),
                ('total_addition_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u63d0\u6210\u603b\u4ef7')),
                ('status', models.SmallIntegerField(choices=[(0, '\u672a\u652f\u4ed8'), (1, '\u5df2\u652f\u4ed8')], default=0, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('user_remark', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u987e\u5ba2\u63cf\u8ff0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0b\u5355\u65f6\u95f4')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.AddressUser', verbose_name='\u8ba2\u5355\u5bc4\u5f80\u5730\u5740')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.Color', verbose_name='\u989c\u8272')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Commodity', verbose_name='\u5546\u54c1')),
                ('proxy_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proxy_user', to=settings.AUTH_USER_MODEL, verbose_name='\u4ee3\u7406\u4eba')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u8868',
                'verbose_name_plural': '\u8ba2\u5355\u8868',
            },
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='\u5c3a\u7801\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u89c4\u683c',
                'verbose_name_plural': '\u5546\u54c1\u89c4\u683c',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='\u6570\u91cf')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.Color', verbose_name='\u989c\u8272')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Commodity', verbose_name='\u5546\u54c1')),
                ('spec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.Spec', verbose_name='\u5546\u54c1\u89c4\u683c')),
            ],
            options={
                'verbose_name': '\u5e93\u5b58',
                'verbose_name_plural': '\u5e93\u5b58',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5206\u7c7b')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.Type', verbose_name='\u7236\u7c7b')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u5206\u7c7b',
                'verbose_name_plural': '\u5546\u54c1\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='UserOpenid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50, verbose_name='openid')),
                ('appid', models.CharField(max_length=50, verbose_name='\u516c\u4f17\u53f7ID')),
                ('head_img', models.ImageField(blank=True, max_length=200, null=True, upload_to='user_head_images/', verbose_name='\u5934\u50cf')),
                ('nickname', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6635\u79f0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237OPENID')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5fae\u4fe1\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u5fae\u4fe1\u4fe1\u606f\u8868',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.Spec', verbose_name='\u89c4\u683c'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Type', verbose_name='\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.CommodtyComment', verbose_name='\u5546\u54c1\u8bc4\u8bba'),
        ),
        migrations.AddField(
            model_name='commentreply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u56de\u590d\u4eba'),
        ),
    ]
