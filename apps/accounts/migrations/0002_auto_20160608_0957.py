# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrutor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Instrutor',
        ),
    ]
