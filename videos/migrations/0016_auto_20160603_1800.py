# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0015_course_bg_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='handout_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='handout_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='order',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='video_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='video_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
