# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20141125_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.URLField(default=b'http://images.puella-magi.net/thumb/2/27/No_Image_Wide.svg/800px-No_Image_Wide.svg.png'),
            preserve_default=True,
        ),
    ]
