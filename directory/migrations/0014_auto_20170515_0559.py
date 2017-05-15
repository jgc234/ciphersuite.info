# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0013_auto_20170515_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfc',
            name='obsoleted_by',
        ),
        migrations.AddField(
            model_name='rfc',
            name='obsoleted_by',
            field=models.ManyToManyField(blank=True, related_name='obsoleted_set', to='directory.Rfc'),
        ),
        migrations.RemoveField(
            model_name='rfc',
            name='obsoletes',
        ),
        migrations.AddField(
            model_name='rfc',
            name='obsoletes',
            field=models.ManyToManyField(blank=True, related_name='obsoleting_set', to='directory.Rfc'),
        ),
    ]