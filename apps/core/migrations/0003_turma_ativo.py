# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160608_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
