# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170507_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='birth_date',
            field=models.DateField(),
        ),
    ]