# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_uid', models.CharField(unique=True, max_length=16)),
                ('keyA', models.CharField(max_length=32)),
                ('keyB', models.CharField(max_length=32)),
                ('owner', models.IntegerField(default=-1)),
                ('counter', models.PositiveIntegerField(default=4294967295)),
                ('revoked', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_uid', models.CharField(max_length=16)),
                ('status', models.SmallIntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('counter', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
