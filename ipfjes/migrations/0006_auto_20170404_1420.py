# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0005_birthplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('initial_consult_reason', models.TextField(null=True, verbose_name=b'What took you to the doctor at the beginning of the illness?', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_diagnosishistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_diagnosishistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Dyspnoea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('breathless', models.NullBooleanField()),
                ('short_of_breath', models.NullBooleanField()),
                ('slower_than_most', models.NullBooleanField()),
                ('stops_for_breath', models.NullBooleanField()),
                ('dressing_undressing', models.NullBooleanField()),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_dyspnoea_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_dyspnoea_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SmokingHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('ever_smoked', models.NullBooleanField()),
                ('current_smoker', models.NullBooleanField()),
                ('start_smoking_age', models.CharField(max_length=20, null=True, blank=True)),
                ('stop_smoking_age', models.CharField(max_length=20, null=True, blank=True)),
                ('cigarettes_per_day', models.CharField(max_length=20, null=True, blank=True)),
                ('what_do_you_smoke', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_smokinghistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_smokinghistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AddField(
            model_name='treatment',
            name='reason_fk',
            field=models.ForeignKey(blank=True, to='opal.Condition', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='reason_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
