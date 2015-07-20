# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='card',
        ),
        migrations.RemoveField(
            model_name='event',
            name='machine',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
