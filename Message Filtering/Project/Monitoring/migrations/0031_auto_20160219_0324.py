# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Monitoring.models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0030_delete_all_msg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msg_comment',
            options={'verbose_name': '2. \u10db\u10d4\u10e1\u10d8\u10ef\u10d8\u10e1 \u10de\u10d0\u10e1\u10e3\u10ee\u10d8', 'verbose_name_plural': '2. \u10db\u10d4\u10e1\u10d8\u10ef\u10d8\u10e1 \u10de\u10d0\u10e1\u10e3\u10ee\u10d8'},
        ),
        migrations.RemoveField(
            model_name='msg_comment',
            name='file_comment_name',
        ),
        migrations.AddField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.CharField(default=1, max_length=300, verbose_name=Monitoring.models.MSG),
            preserve_default=False,
        ),
    ]
