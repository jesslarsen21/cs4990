# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0003_auto_20151021_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='Author',
            new_name='author',
        ),
    ]
