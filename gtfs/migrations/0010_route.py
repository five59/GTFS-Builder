# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0009_stop_parent_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('route_id', models.CharField(max_length=100)),
                ('route_short_name', models.CharField(max_length=100)),
                ('route_long_name', models.CharField(max_length=200)),
                ('route_desc', models.CharField(default='', max_length=255, blank=True)),
                ('route_type', models.CharField(default='0', max_length=1, choices=[(b'0', b'Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area.'), (b'1', b'Subway, Metro. Any underground rail system within a metropolitan area.'), (b'2', b'Rail. Used for intercity or long-distance travel.'), (b'3', b'Bus. Used for short- and long-distance bus routes.'), (b'4', b'Ferry. Used for short- and long-distance boat service.'), (b'5', b'Cable car. Used for street-level cable cars where the cable runs beneath the car.'), (b'6', b'Gondola, Suspended cable car. Typically used for aerial cable cars where the car is suspended from the cable.'), (b'7', b'Funicular. Any rail system designed for steep inclines.')])),
                ('route_url', models.URLField(default='', blank=True)),
                ('route_color', models.CharField(default='', max_length=6, blank=True)),
                ('route_text_color', models.CharField(default='', max_length=6, blank=True)),
                ('agency', models.ForeignKey(to='gtfs.Agency')),
            ],
            options={
                'ordering': ['agency__agency_name', 'route_short_name'],
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
    ]
