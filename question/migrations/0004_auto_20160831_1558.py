# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-31 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20160831_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(blank=True, to='question.Tag'),
        ),
    ]