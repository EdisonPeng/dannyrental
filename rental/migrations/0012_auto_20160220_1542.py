# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0011_auto_20160220_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccontent',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='topiccontent',
            name='subtopic',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
