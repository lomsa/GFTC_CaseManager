# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0025_auto_20160218_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg_comment',
            old_name='file_body',
            new_name='file_comment_body',
        ),
        migrations.AlterField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]