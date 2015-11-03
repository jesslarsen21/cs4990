# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0005_tweet_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='author',
        ),
    ]
