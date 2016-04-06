# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0011_auto_20160212_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status1',
            field=models.CharField(unique=True, max_length=300),
        ),
    ]
