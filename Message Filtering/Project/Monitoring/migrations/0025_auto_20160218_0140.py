# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 09:40
from __future__ import unicode_literals

import Monitoring.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0024_auto_20160218_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.CharField(max_length=300, null=True, verbose_name=Monitoring.models.MSG),
        ),
    ]
