# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0021_auto_20160218_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg',
            old_name='file_name',
            new_name='Transaction_Reference_Number',
        ),
    ]
