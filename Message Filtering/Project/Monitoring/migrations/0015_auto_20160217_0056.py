# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0014_remove_customer_status1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ip',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]