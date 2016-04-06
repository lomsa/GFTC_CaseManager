# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, blank=True)),
            ],
            options={
                'verbose_name': '1. \u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0',
                'verbose_name_plural': '1. \u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, blank=True)),
                ('bic', models.CharField(max_length=150, blank=True)),
                ('address', models.CharField(max_length=150, blank=True)),
                ('receive_newsletter', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '2. \u10dd\u10e0\u10d2\u10d0\u10dc\u10d8\u10d6\u10d0\u10ea\u10d8\u10d0',
                'verbose_name_plural': '2. \u10dd\u10e0\u10d2\u10d0\u10dc\u10d8\u10d6\u10d0\u10ea\u10d8\u10d4\u10d1\u10d8',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mob', models.CharField(max_length=150, blank=True)),
                ('tel', models.CharField(max_length=150, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('category', models.ManyToManyField(related_name='category', to='Monitoring.UserCategory', blank=True)),
                ('group', models.ManyToManyField(related_name='group', to='Monitoring.UserGroup', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '3. \u10db\u10dd\u10db\u10ee\u10db\u10d0\u10e0\u10d4\u10d1\u10da\u10d8\u10e1 \u10de\u10e0\u10dd\u10e4\u10d8\u10da\u10d8',
                'verbose_name_plural': '3. \u10db\u10dd\u10db\u10ee\u10db\u10d0\u10e0\u10d4\u10d1\u10da\u10d8\u10e1 \u10de\u10e0\u10dd\u10e4\u10d8\u10da\u10d8',
            },
        ),
    ]
