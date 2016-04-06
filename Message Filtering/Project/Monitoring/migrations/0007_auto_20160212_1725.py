# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0006_auto_20160212_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='result',
            field=models.CharField(unique=True, max_length=300),
        ),
    ]
