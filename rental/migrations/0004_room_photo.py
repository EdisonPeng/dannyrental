# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_auto_20150703_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.ImageField(upload_to=b'images/room_photo/', blank=True),
        ),
    ]
