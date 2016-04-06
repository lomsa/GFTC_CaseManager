# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0008_remove_customer_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ip',
            field=models.IPAddressField(unique=True),
        ),
    ]
