# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('agency_id', models.CharField(help_text='The agency_id field is an ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency.', max_length=64, null=True, verbose_name='Agency ID', blank=True)),
                ('agency_name', models.CharField(help_text='The agency_name field contains the full name of the transit agency. Google Maps will display this name.', max_length=255, verbose_name='Agency Name')),
                ('agency_url', models.URLField(help_text='The agency_url field contains the URL of the transit agency. The value must be a fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.', max_length=255)),
                ('agency_phone', models.CharField(default='', help_text='The agency_phone field contains a single voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency\'s service area. It can and should contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet\'s "503-238-RIDE") is permitted, but the field must not contain any other descriptive text.', max_length=20, blank=True)),
                ('agency_fare_url', models.URLField(default='', help_text='The agency_fare_url specifies the URL of a web page that allows a rider to purchase tickets or other fare instruments for that agency online. The value must be a fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.', max_length=255, blank=True)),
            ],
            options={
                'ordering': ['agency_id'],
                'verbose_name': 'Agency',
                'verbose_name_plural': 'Agencies',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('iso_639_1', models.CharField(default=b'', help_text='ISO 639-1 alpha-2 language code.', unique=True, max_length=2, blank=True)),
                ('name', models.CharField(help_text='English name of language.', unique=True, max_length=128)),
            ],
            options={
                'ordering': ['iso_639_1'],
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('iso_3166_2', models.CharField(default=b'', help_text='ISO 3166 2-character country code.', unique=True, max_length=2, blank=True)),
                ('zone_name', models.CharField(help_text='Zone name used in value of TZ environment variable.', unique=True, max_length=128)),
            ],
            options={
                'ordering': ['iso_3166_2'],
                'verbose_name': 'Timezone',
                'verbose_name_plural': 'Timezones',
            },
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_lang',
            field=models.ForeignKey(to='gtfs.Language', help_text="A two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). This setting defines capitalization rules and other language-specific settings for all text contained in this transit agency's feed.", null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_timezone',
            field=models.ForeignKey(help_text='The agency_timezone field contains the timezone where the transit agency is located. Timezone names never contain the space character but may contain an underscore. If multiple agencies are specified in the feed, each must have the same agency_timezone.', to='gtfs.Timezone'),
        ),
    ]
