# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0028_auto_20170505_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPFJESEthnicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'IPFJES Ethnicities',
            },
        ),
    ]
