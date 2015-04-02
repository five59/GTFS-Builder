# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0004_auto_20150401_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='iso_639_1',
            field=models.CharField(default=b'', help_text='ISO 639-1 alpha-2 language code.', unique=True, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='English name of language.', unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='timezone',
            name='iso_3166_2',
            field=models.CharField(default=b'', help_text='ISO 3166 2-character country code.', unique=True, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='timezone',
            name='zone_name',
            field=models.CharField(help_text='Zone name used in value of TZ environment variable.', unique=True, max_length=128),
        ),
    ]
