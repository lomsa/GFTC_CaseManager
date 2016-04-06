# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0027_auto_20160218_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=8000, blank=True)),
            ],
            options={
                'verbose_name': '1. \u10e7\u10d5\u10d4\u10da\u10d0 \u10db\u10d4\u10e1\u10d8\u10ef\u10d8',
                'verbose_name_plural': '1. \u10e7\u10d5\u10d4\u10da\u10d0 \u10db\u10d4\u10e1\u10d8\u10ef\u10d8',
            },
        ),
    ]
