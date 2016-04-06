# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0028_all_msg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='all_msg',
            options={'verbose_name': '1. \u10e7\u10d5\u10d4\u10da\u10d0 20 \u10d3\u10d0 21 \u10db\u10d4\u10e1\u10d8\u10ef\u10d8', 'verbose_name_plural': '1. \u10e7\u10d5\u10d4\u10da\u10d0 20 \u10d3\u10d0 21 \u10db\u10d4\u10e1\u10d8\u10ef\u10d8'},
        ),
        migrations.RenameField(
            model_name='all_msg',
            old_name='text',
            new_name='text20',
        ),
        migrations.AddField(
            model_name='all_msg',
            name='text21',
            field=models.TextField(max_length=8000, blank=True),
        ),
    ]
