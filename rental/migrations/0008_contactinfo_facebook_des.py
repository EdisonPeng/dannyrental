# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_contactinfo_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='facebook_des',
            field=models.CharField(default="Danny's House", max_length=50),
            preserve_default=False,
        ),
    ]
