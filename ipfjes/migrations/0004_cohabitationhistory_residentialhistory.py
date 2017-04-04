# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0003_auto_20170404_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='CohabitationHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('nameofperson', models.CharField(max_length=250, null=True, blank=True)),
                ('relationship', models.CharField(max_length=250, null=True, blank=True)),
                ('howlong', models.TextField(null=True, blank=True)),
                ('occupation', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_cohabitationhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_cohabitationhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ResidentialHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('address', models.TextField(null=True, blank=True)),
                ('howlong', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_residentialhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_residentialhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
