# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0006_auto_20150401_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timezone',
            name='note',
        ),
    ]
