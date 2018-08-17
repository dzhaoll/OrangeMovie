# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-07 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, verbose_name='用户名')),
                ('upwd', models.CharField(max_length=40, verbose_name='密码')),
                ('uemail', models.CharField(max_length=40, verbose_name='邮箱')),
                ('uphone', models.CharField(max_length=20, verbose_name='手机')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='注册时间')),
                ('isban', models.BooleanField(default=False, verbose_name='禁用')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
