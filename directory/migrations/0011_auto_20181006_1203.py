# Generated by Django 2.1 on 2018-10-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0010_auto_20180719_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='TlsVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
            ],
            options={
                'verbose_name': 'TLS version',
                'verbose_name_plural': 'TLS versions',
                'ordering': ['major', 'minor'],
            },
        ),
        migrations.RemoveField(
            model_name='ciphersuite',
            name='tls_version',
        ),
        migrations.AddField(
            model_name='ciphersuite',
            name='tls_version',
            field=models.ManyToManyField(blank=True, to='directory.TlsVersion', verbose_name='TLS version'),
        ),
    ]
