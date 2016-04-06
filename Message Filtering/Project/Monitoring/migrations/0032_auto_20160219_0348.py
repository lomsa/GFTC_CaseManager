# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0031_auto_20160219_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.CharField(max_length=300),
        ),
    ]
