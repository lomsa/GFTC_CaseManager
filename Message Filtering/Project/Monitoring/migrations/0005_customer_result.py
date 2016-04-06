# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='result',
            field=models.TextField(default=1, unique=True, max_length=300),
            preserve_default=False,
        ),
    ]
