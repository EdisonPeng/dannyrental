# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0009_auto_20160220_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
