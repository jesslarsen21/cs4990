# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='punch',
            options={'verbose_name_plural': 'punches'},
        ),
        migrations.AlterField(
            model_name='punch',
            name='note',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='punch',
            name='time_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
