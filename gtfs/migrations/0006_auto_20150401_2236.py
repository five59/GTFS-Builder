# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0005_auto_20150401_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timezone',
            options={'ordering': ['name'], 'verbose_name': 'Timezone', 'verbose_name_plural': 'Timezones'},
        ),
        migrations.RenameField(
            model_name='timezone',
            old_name='zone_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='timezone',
            name='iso_3166_2',
        ),
        migrations.AddField(
            model_name='timezone',
            name='note',
            field=models.CharField(default='', max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='timezone',
            name='utc_offset',
            field=models.CharField(default='', max_length=10, blank=True),
        ),
    ]
