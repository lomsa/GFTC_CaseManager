# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0035_msg_io'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.ForeignKey(to='Monitoring.MSG', max_length=300),
        ),
    ]
