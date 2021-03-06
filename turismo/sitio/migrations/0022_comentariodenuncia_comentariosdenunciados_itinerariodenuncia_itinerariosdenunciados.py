# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0021_auto_20170525_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioDenuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitio.Comentario')),
                ('usuario_denunciante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComentariosDenunciados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('comentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitio.Comentario')),
                ('usuario_denunciado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItinerarioDenuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitio.Itinerario')),
                ('usuario_denunciante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItinerariosDenunciados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('itinerario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitio.Itinerario')),
                ('usuario_denunciado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
