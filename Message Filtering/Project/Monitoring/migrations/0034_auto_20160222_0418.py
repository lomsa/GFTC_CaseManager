# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0033_auto_20160222_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg',
            old_name='data',
            new_name='day',
        ),
        migrations.AddField(
            model_name='msg',
            name='time',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
