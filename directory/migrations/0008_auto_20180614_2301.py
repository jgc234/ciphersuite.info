# Generated by Django 2.0.6 on 2018-06-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_auto_20171217_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='glyphicon',
            field=models.CharField(help_text='For reference, see https://getbootstrap.com/docs/3.3/components', max_length=50),
        ),
    ]