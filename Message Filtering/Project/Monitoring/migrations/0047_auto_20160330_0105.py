# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0046_auto_20160328_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='comment_70',
        ),
        migrations.RemoveField(
            model_name='msg',
            name='comment_77a',
        ),
        migrations.RemoveField(
            model_name='msg',
            name='orig_date',
        ),
        migrations.RemoveField(
            model_name='msg',
            name='queaies_75',
        ),
        migrations.RemoveField(
            model_name='msg',
            name='refernce_21',
        ),
    ]
