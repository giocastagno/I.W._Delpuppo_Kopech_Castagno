# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0015_auto_20170524_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntaje',
            name='calificacion',
            field=models.IntegerField(choices=[(0, ''), (1, 'Malo'), (2, 'Regular'), (3, 'Bueno'), (4, 'Muy Bueno'), (5, 'Excelente')], default=0),
        ),
    ]
