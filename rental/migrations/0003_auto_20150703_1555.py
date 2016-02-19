# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20150703_1546'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Location',
            new_name='Transportation',
        ),
    ]
