# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0023_auto_20170526_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariosdenunciados',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itinerariosdenunciados',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
