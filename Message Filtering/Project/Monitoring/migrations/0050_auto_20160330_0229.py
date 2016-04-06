# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0049_auto_20160330_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg195',
            name='input',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='msg195',
            name='output',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
