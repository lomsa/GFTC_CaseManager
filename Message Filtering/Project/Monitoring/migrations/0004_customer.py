# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0003_auto_20160212_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=300)),
                ('name', models.CharField(unique=True, max_length=300)),
                ('ip', models.IPAddressField(unique=True)),
            ],
            options={
                'verbose_name': '1. \u10db\u10d8\u10e1\u10d0\u10db\u10d0\u10e0\u10d7\u10d8',
                'verbose_name_plural': '1. \u10db\u10d8\u10e1\u10d0\u10db\u10d0\u10e0\u10d7\u10d8',
            },
        ),
    ]
