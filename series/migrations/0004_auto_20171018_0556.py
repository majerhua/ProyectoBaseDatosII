# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20171018_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='observacion',
            field=models.TextField(max_length=500),
        ),
    ]