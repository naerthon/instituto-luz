# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160821_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='data_inicio',
            field=models.DateField(verbose_name='Data de início'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_termino',
            field=models.DateField(verbose_name='Data de término'),
        ),
    ]
