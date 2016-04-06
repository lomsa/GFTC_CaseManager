# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0037_auto_20160224_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg_comment',
            name='kay',
            field=models.ForeignKey(default=1, to='Monitoring.MSG'),
            preserve_default=False,
        ),
    ]
