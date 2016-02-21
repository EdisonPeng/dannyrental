# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0013_auto_20160220_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='about_photo',
        ),
        migrations.RemoveField(
            model_name='home',
            name='room_photo',
        ),
        migrations.RemoveField(
            model_name='home',
            name='transportation_photo',
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
    ]
