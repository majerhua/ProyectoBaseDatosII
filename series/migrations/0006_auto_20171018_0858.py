# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_remove_proyectodocs_coddoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectocosto',
            name='observacion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='proyectodocs',
            name='observacion',
            field=models.TextField(max_length=500),
        ),
    ]
