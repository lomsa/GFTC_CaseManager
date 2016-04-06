# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0048_remove_msg_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSG195',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=300)),
                ('reciver', models.CharField(max_length=300)),
                ('name75', models.CharField(max_length=300)),
                ('comment77a', models.CharField(max_length=300)),
                ('comment70', models.CharField(max_length=300)),
                ('description79', models.TextField(max_length=300)),
                ('data11a', models.CharField(max_length=300)),
                ('kay', models.ForeignKey(to='Monitoring.MSG')),
            ],
            options={
                'verbose_name': '\u10db\u10d4\u10e1\u10d8\u10ef\u10d8 195',
                'verbose_name_plural': '\u10db\u10d4\u10e1\u10d8\u10ef\u10d8 195',
            },
        ),
        migrations.DeleteModel(
            name='MSG_COMMENT',
        ),
    ]
