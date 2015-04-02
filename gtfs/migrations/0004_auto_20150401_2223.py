# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0003_auto_20150401_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='iso_639_1',
            field=models.CharField(default=b'', help_text='ISO 639-1 alpha-2 language code.', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='English name of language.', max_length=128),
        ),
    ]
