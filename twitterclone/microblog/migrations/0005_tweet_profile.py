# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0004_auto_20151021_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='profile',
            field=models.ForeignKey(default=0, to='microblog.Profile'),
            preserve_default=False,
        ),
    ]
