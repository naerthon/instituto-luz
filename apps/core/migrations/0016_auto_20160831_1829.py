# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20160831_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='curso',
            field=models.CharField(choices=[('1', 'Conheça o espiritísmo'), ('2', 'Nosso Lar'), ('3', 'Passe'), ('4', 'Corrente Magnética')], default='1', max_length=1, verbose_name='Curso'),
        ),
    ]
