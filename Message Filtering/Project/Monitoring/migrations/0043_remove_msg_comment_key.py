# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0042_msg_comment_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg_comment',
            name='key',
        ),
    ]
