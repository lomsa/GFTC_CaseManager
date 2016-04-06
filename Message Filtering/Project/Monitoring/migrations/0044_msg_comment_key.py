# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0043_remove_msg_comment_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg_comment',
            name='key',
            field=models.ForeignKey(default=1, to='Monitoring.MSG'),
            preserve_default=False,
        ),
    ]
