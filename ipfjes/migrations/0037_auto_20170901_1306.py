# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0036_radiology'),
    ]

    operations = [
        migrations.CreateModel(
            name='CtAndBiopsy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('ct_findings', models.CharField(blank=True, max_length=12, null=True, choices=[(b'no CT', b'no CT'), (b'definite UIP', b'definite UIP'), (b'possible UIP', b'possible UIP'), (b'other', b'other')])),
                ('ct_findings_other', models.TextField(null=True, verbose_name=b'Other CT Findings Description', blank=True)),
                ('biopsy_findings', models.CharField(blank=True, max_length=12, null=True, choices=[(b'no Biopsy', b'no Biopsy'), (b'definite UIP', b'definite UIP'), (b'possible UIP', b'possible UIP'), (b'other', b'other')])),
                ('biopsy_findings_other', models.TextField(null=True, verbose_name=b'Other Biopsy Findings Description', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_ctandbiopsy_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_ctandbiopsy_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='radiology',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='radiology',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='radiology',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Radiology',
        ),
    ]
