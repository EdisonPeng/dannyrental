# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_contactinfo_facebook_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='facebook_des',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='line_photo',
            field=models.ImageField(upload_to=b'images/contact_photo/', blank=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='wechat',
            field=models.CharField(default='wechattogether', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='wechat_photo',
            field=models.ImageField(upload_to=b'images/contact_photo/', blank=True),
        ),
    ]
