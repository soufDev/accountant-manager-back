# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
