# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0010_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(default='', max_length=128, verbose_name=b'Name', blank=True)),
                ('note', models.TextField(default='', verbose_name='Notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Data Set',
                'verbose_name_plural': 'Data Sets',
            },
        ),
        migrations.AlterField(
            model_name='stop',
            name='wheelchair_boarding',
            field=models.CharField(default=b'0', help_text='The wheelchair_boarding field identifies whether wheelchair boardings are possible from the specified stop or station.', max_length=1, choices=[(b'0', 'No Accessibility Info Available'), (b'1', 'Some vehicles at this stop can be boarded by a rider in a wheelchair'), (b'2', 'Wheelchair boarding is not possible.')]),
        ),
        migrations.AddField(
            model_name='agency',
            name='data_set',
            field=models.ForeignKey(to='gtfs.DataSet', null=True),
        ),
    ]
