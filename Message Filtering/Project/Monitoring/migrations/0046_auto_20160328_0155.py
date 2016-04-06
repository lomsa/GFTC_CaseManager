# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0045_remove_msg_comment_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='comment_70',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='msg',
            name='comment_77a',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='msg',
            name='orig_date',
            field=models.CharField(max_length=8000, blank=True),
        ),
        migrations.AddField(
            model_name='msg',
            name='queaies_75',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='msg',
            name='refernce_21',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
