# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_course_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseCategory',
            new_name='Category',
        ),
    ]