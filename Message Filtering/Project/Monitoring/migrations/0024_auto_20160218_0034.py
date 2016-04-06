# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0023_auto_20160218_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg_comment',
            name='Related_Reference',
        ),
        migrations.AddField(
            model_name='msg_comment',
            name='file_body',
            field=models.TextField(blank=True, max_length=8000),
        ),
        migrations.AddField(
            model_name='msg_comment',
            name='file_comment_name',
            field=models.ForeignKey(blank=True, default=1, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='Monitoring.MSG'),
            preserve_default=False,
        ),
    ]
