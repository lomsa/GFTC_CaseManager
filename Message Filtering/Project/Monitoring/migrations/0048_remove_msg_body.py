# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0047_auto_20160330_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='body',
        ),
    ]
