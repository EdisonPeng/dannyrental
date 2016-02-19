# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_room_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'images/about_photo/')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RoomPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'images/room_photo/')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='photo',
        ),
        migrations.AddField(
            model_name='roomphoto',
            name='room',
            field=models.ForeignKey(to='rental.Room'),
        ),
        migrations.AddField(
            model_name='aboutphoto',
            name='room',
            field=models.ForeignKey(to='rental.Room'),
        ),
    ]
