# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0011_auto_20150402_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('trip_id', models.CharField(max_length=128, verbose_name='Service ID')),
                ('headsign', models.CharField(default='', max_length=128, verbose_name='Headsign', blank=True)),
                ('short_name', models.CharField(default='', max_length=128, verbose_name='Short Name', blank=True)),
                ('direction', models.CharField(default='0', max_length=1, verbose_name=b'Direction', choices=[(b'0', b'Primary/Outbound Direction'), (b'1', b'Secondary/Inbound Direction')])),
                ('block_id', models.CharField(default='', max_length=128, verbose_name='Block ID', blank=True)),
                ('wheelchair_accessible', models.CharField(default='0', max_length=1, verbose_name='Bicycle Allowance', choices=[(b'0', b'No Bike Info Available'), (b'1', b'Bicycles Are Allowed'), (b'2', b'Bicycles Are Not Allowed')])),
                ('route', models.ForeignKey(to='gtfs.Route')),
            ],
            options={
                'ordering': ['trip_id'],
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
    ]
