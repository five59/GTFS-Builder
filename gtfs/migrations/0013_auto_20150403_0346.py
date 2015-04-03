# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0012_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='bike_access',
            field=models.CharField(default='0', max_length=1, verbose_name='Bicycle Allowance', choices=[(b'0', b'No Bike Info Available'), (b'1', b'Bicycles Are Allowed'), (b'2', b'Bicycles Are Not Allowed')]),
        ),
        migrations.AlterField(
            model_name='trip',
            name='block_id',
            field=models.CharField(default='', help_text='The block_id field identifies the block to which the trip belongs. A block consists of two or more sequential trips made using the same vehicle, where a passenger can transfer from one trip to the next just by staying in the vehicle. The block_id must be referenced by two or more trips in trips.txt.', max_length=128, verbose_name='Block ID', blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='headsign',
            field=models.CharField(default='', help_text="The trip_headsign field contains the text that appears on a sign that identifies the trip's destination to passengers. Use this field to distinguish between different patterns of service in the same route. If the headsign changes during a trip, you can override the trip_headsign by specifying values for the the stop_headsign field in stop_times.txt.", max_length=128, verbose_name='Headsign', blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='short_name',
            field=models.CharField(default='', help_text='The trip_short_name field contains the text that appears in schedules and sign boards to identify the trip to passengers, for example, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, please leave this field blank. A trip_short_name value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations.', max_length=128, verbose_name='Short Name', blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(help_text='The trip_id field contains an ID that identifies a trip. The trip_id is dataset unique.', max_length=128, verbose_name='Trip ID'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='wheelchair_accessible',
            field=models.CharField(default='0', max_length=1, verbose_name='Wheelchair Accessibility', choices=[(b'0', b'No Accessibility Info'), (b'1', b'Vehicle Can Accommodate at Least One Wheelchair'), (b'2', b'No Wheelchairs Can be Accommodated')]),
        ),
    ]
