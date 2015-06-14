# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('long_position', models.DecimalField(max_digits=9, decimal_places=6)),
                ('lat_position', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
            options={
                'db_table': 'Address',
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresss',
            },
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('address', models.ForeignKey(to='address.Address')),
            ],
            options={
                'db_table': 'Address_detail',
                'verbose_name': 'Address_detail',
                'verbose_name_plural': 'Address_details',
            },
        ),
    ]
