# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0026_auto_20160218_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg_comment',
            name='file_comment_name',
        ),
        migrations.AddField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.ManyToManyField(to='Monitoring.MSG', max_length=300),
        ),
    ]
