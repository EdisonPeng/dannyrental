# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0010_reservation_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtopic', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='name',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='description',
        ),
        migrations.AddField(
            model_name='topiccontent',
            name='reservation',
            field=models.ForeignKey(to='rental.Reservation'),
        ),
    ]
