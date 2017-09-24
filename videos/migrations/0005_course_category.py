# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_coursecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.CourseCategory'),
        ),
    ]