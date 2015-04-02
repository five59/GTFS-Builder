# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0008_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='parent_station',
            field=models.ForeignKey(to='gtfs.Stop', help_text='For stops that are physically located inside stations, the parent_station field identifies the station associated with the stop. To use this field, stops.txt must also contain a row where this stop ID is assigned as a station.', null=True),
        ),
    ]
