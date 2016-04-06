# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0050_auto_20160330_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg195',
            name='referance21',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='msg195',
            name='reference20',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
