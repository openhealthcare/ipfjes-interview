# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0024_auto_20170426_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScarringDrugs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('amiodarone', models.BooleanField(default=False)),
                ('flecainade', models.BooleanField(default=False)),
                ('nitrofurantoin', models.BooleanField(default=False)),
                ('azathioprine', models.BooleanField(default=False)),
                ('gefitinib', models.BooleanField(default=False)),
                ('ifosfamide', models.BooleanField(default=False)),
                ('melphalan', models.BooleanField(default=False)),
                ('rituximab', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_scarringdrugs_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_scarringdrugs_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
