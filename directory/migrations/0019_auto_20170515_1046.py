# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0018_auto_20170515_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rfc',
            old_name='cipher_suites',
            new_name='defined_cipher_suites',
        ),
        migrations.RenameField(
            model_name='rfc',
            old_name='year',
            new_name='release_year',
        ),
        migrations.RemoveField(
            model_name='ciphersuite',
            name='related_rfcs',
        ),
        migrations.RemoveField(
            model_name='encalgorithm',
            name='vulnerability',
        ),
        migrations.RemoveField(
            model_name='kexalgorithm',
            name='vulnerability',
        ),
        migrations.RemoveField(
            model_name='macalgorithm',
            name='vulnerability',
        ),
        migrations.RemoveField(
            model_name='protocolversion',
            name='vulnerability',
        ),
        migrations.RemoveField(
            model_name='rfc',
            name='obsoleted_by',
        ),
        migrations.RemoveField(
            model_name='rfc',
            name='obsoletes',
        ),
        migrations.AddField(
            model_name='encalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='kexalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='macalgorithm',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='protocolversion',
            name='vulnerabilities',
            field=models.ManyToManyField(blank=True, to='directory.Vulnerability'),
        ),
        migrations.AddField(
            model_name='rfc',
            name='related_documents',
            field=models.ManyToManyField(blank=True, related_name='_rfc_related_documents_+', to='directory.Rfc', verbose_name='Related RFCs'),
        ),
        migrations.AlterField(
            model_name='ciphersuite',
            name='protocol_version',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='directory.ProtocolVersion', verbose_name='Protocol'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]