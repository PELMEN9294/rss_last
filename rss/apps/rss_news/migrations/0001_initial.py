# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
