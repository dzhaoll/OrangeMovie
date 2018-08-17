# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-22 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_comment_com_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='star',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=100, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='mtype',
            field=models.CharField(max_length=50, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.CharField(max_length=200, verbose_name='海报'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='scriptwriter',
            field=models.CharField(max_length=500, verbose_name='编剧'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=50, verbose_name='片名'),
        ),
    ]
