# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timezone',
            name='iso_3166_2',
            field=models.CharField(default=b'', help_text='ISO 3166 2-character country code.', max_length=2, blank=True),
        ),
    ]
