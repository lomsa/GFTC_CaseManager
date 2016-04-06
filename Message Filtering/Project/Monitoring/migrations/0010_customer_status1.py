# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0009_auto_20160212_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status1',
            field=models.CharField(default=1, unique=True, max_length=300),
            preserve_default=False,
        ),
    ]
