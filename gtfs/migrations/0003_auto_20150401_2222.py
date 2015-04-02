# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0002_auto_20150401_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timezone',
            name='zone_name',
            field=models.CharField(help_text='Zone name used in value of TZ environment variable.', max_length=128),
        ),
    ]
