# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0004_cohabitationhistory_residentialhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('place', models.TextField(null=True, blank=True)),
                ('countryofbirth_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('countryofbirth_fk', models.ForeignKey(blank=True, to='opal.Destination', null=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_birthplace_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_birthplace_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
