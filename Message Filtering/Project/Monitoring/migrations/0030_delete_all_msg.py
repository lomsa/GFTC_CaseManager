# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monitoring', '0029_auto_20160218_2355'),
    ]

    operations = [
        migrations.DeleteModel(
            name='All_Msg',
        ),
    ]
