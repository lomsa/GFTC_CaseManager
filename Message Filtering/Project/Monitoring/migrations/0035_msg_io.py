# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0034_auto_20160222_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='io',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
