# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0013_auto_20160212_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='status1',
        ),
    ]
