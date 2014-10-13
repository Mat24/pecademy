# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(verbose_name=b'fecha creacion')),
                ('fecha_actualizacion', models.DateTimeField(verbose_name=b'fecha actulizacion')),
                ('contenido', models.TextField()),
                ('titulo', models.CharField(max_length=200)),
                ('estado', models.IntegerField(default=0, editable=False, blank=True)),
                ('con_vistas', models.IntegerField(default=0, editable=False, blank=True)),
                ('etiqueas', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to=b'templates/static/media/upload/blog')),
                ('comentario', models.CharField(max_length=200)),
                ('estado_comentario', models.IntegerField(default=0, editable=False, blank=True)),
                ('con_comentarios', models.IntegerField(default=0, editable=False, blank=True)),
                ('usuario', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(verbose_name=b'fecha de publicacion de comentario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
