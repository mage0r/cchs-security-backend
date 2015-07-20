# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0003_auto_20150623_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(default=b'Machine Operation', max_length=32, editable=False)),
                ('event_text', models.TextField(null=True, editable=False, blank=True)),
                ('card', models.ForeignKey(blank=True, editable=False, to='cards.Card', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
                ('active', models.BooleanField(default=False)),
                ('minimum_level', models.CharField(default=0, max_length=3, choices=[(b'0', b'Not Cleared'), (b'1', b'Operator'), (b'2', b'Instructor')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MachineAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=0, max_length=3, choices=[(b'0', b'Not Cleared'), (b'1', b'Operator'), (b'2', b'Instructor')])),
                ('machine', models.ForeignKey(to='machines.Machine')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='machine',
            field=models.ForeignKey(blank=True, editable=False, to='machines.Machine', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
