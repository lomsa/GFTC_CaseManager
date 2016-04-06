# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0010_customer_status1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status1',
            field=models.CharField(max_length=300),
        ),
    ]
