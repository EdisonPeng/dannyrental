# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20150704_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_photo', models.ImageField(upload_to=b'images/home_photo/')),
                ('about_photo', models.ImageField(upload_to=b'images/home_photo/')),
                ('transportation_photo', models.ImageField(upload_to=b'images/home_photo/')),
            ],
        ),
        migrations.CreateModel(
            name='HomePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'images/about_photo/')),
                ('description', models.CharField(max_length=50, blank=True)),
                ('room', models.ForeignKey(to='rental.Home')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutphoto',
            name='room',
        ),
        migrations.RemoveField(
            model_name='roomphoto',
            name='description',
        ),
        migrations.DeleteModel(
            name='AboutPhoto',
        ),
    ]
