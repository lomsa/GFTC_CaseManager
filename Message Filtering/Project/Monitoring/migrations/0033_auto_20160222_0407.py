# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0032_auto_20160219_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='bic',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='msg',
            name='data',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='msg',
            name='mt',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
