# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-09 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=200, verbose_name='密码'),
        ),
    ]
