# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-22 01:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='allow_pinning',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='copyright_owner',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='copyright_status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='credit_line',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hide_from_searches',
        ),
    ]
