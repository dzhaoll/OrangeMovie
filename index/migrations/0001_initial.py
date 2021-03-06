# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-07 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(verbose_name='分数')),
                ('content', models.CharField(max_length=1000, verbose_name='评论')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='片名')),
                ('country', models.CharField(max_length=20, verbose_name='国家')),
                ('date', models.CharField(max_length=50, verbose_name='时间')),
                ('mtype', models.CharField(max_length=20, verbose_name='类型')),
                ('language', models.CharField(max_length=30, verbose_name='语言')),
                ('director', models.CharField(max_length=200, verbose_name='导演')),
                ('actor', models.CharField(max_length=500, verbose_name='主演')),
                ('scriptwriter', models.CharField(max_length=200, verbose_name='编剧')),
                ('introduction', models.CharField(max_length=1000, verbose_name='简介')),
                ('picture', models.ImageField(default='normal.jpg', upload_to='static/images/movie', verbose_name='海报')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo'),
        ),
    ]
