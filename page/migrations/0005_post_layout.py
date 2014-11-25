# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20141125_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='layout',
            field=models.CharField(default=b'one', max_length=50),
            preserve_default=True,
        ),
    ]
