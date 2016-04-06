# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0051_auto_20160330_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg195',
            old_name='input',
            new_name='input_output',
        ),
        migrations.RemoveField(
            model_name='msg195',
            name='output',
        ),
    ]
