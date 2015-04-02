# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0007_remove_timezone_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('stop_id', models.CharField(help_text='The stop_id field contains an ID that uniquely identifies a stop or station. Multiple routes may use the same stop. The stop_id is dataset unique.', max_length=128)),
                ('code', models.CharField(default='', help_text='The stop_code field contains short text or a number that uniquely identifies the stop for passengers. Stop codes are often used in phone-based transit information systems or printed on stop signage to make it easier for riders to get a stop schedule or real-time arrival information for a particular stop. The stop_code field should only be used for stop codes that are displayed to passengers. For internal codes, use stop_id. This field should be left blank for stops without a code.', max_length=128, blank=True)),
                ('name', models.CharField(help_text='The stop_name field contains the name of a stop or station. Please use a name that people will understand in the local and tourist vernacular.', max_length=200)),
                ('desc', models.CharField(default='', help_text='The stop_desc field contains a description of a stop. Please provide useful, quality information. Do not simply duplicate the name of the stop.', max_length=255, blank=True)),
                ('lat', models.DecimalField(help_text='The stop_lat field contains the latitude of a stop or station. The field value must be a valid WGS 84 latitude.', max_digits=9, decimal_places=6)),
                ('lon', models.DecimalField(help_text='The stop_lon field contains the longitude of a stop or station. The field value must be a valid WGS 84 longitude value from -180 to 180.', max_digits=9, decimal_places=6)),
                ('zone_id', models.CharField(default='', help_text='The zone_id field defines the fare zone for a stop ID. Zone IDs are required if you want to provide fare information using fare_rules.txt. If this stop ID represents a station, the zone ID is ignored.', max_length=100, blank=True)),
                ('url', models.URLField(default='', help_text='The stop_url field contains the URL of a web page about a particular stop. This should be different from the agency_url and the route_url fields.', blank=True)),
                ('location_type', models.CharField(default=b'0', help_text='The location_type field identifies whether this stop ID represents a stop or station. Stations may have different properties from stops when they are represented on a map or used in trip planning.', max_length=1, choices=[(b'0', 'Stop'), (b'1', 'Station')])),
                ('wheelchair_boarding', models.CharField(default=b'0', help_text='The wheelchair_boarding field identifies whether wheelchair boardings are possible from the specified stop or station.', max_length=1, choices=[(b'0', 'No Accessibility Info Available'), (b'0', 'Some vehicles at this stop can be boarded by a rider in a wheelchair'), (b'0', 'Wheelchair boarding is not possible.')])),
                ('timezone', models.ForeignKey(to='gtfs.Timezone', help_text='The agency_timezone field contains the timezone where the transit agency is located. Timezone names never contain the space character but may contain an underscore. If multiple agencies are specified in the feed, each must have the same agency_timezone.', null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Stop',
                'verbose_name_plural': 'Stops',
            },
        ),
    ]
