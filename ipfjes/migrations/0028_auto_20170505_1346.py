# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0027_auto_20170505_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsbestosExposureScreening',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('exposed', models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('description', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_asbestosexposurescreening_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_asbestosexposurescreening_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AsbestosLocalControl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='asbestosexposurehistory',
            name='asbestos_material_fk',
        ),
        migrations.RemoveField(
            model_name='asbestosexposurehistory',
            name='asbestos_material_ft',
        ),
        migrations.RemoveField(
            model_name='asbestosexposurehistory',
            name='percent_task',
        ),
        migrations.RemoveField(
            model_name='asbestosexposurehistory',
            name='task_location_fk',
        ),
        migrations.RemoveField(
            model_name='asbestosexposurehistory',
            name='task_location_ft',
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='asbestos_percentage',
            field=models.CharField(blank=True, max_length=b'100', null=True, choices=[(b'100%', b'100%'), (b'20 - 40%', b'20 - 40%'), (b'10 - 15%', b'10 - 15%'), (b'1%', b'1%')]),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='asbestos_type',
            field=models.CharField(blank=True, max_length=b'100', null=True, choices=[(b'Amosite or crocidolite', b'Amosite or crocidolite'), (b'Chrysotile', b'Chrysotile')]),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='local_controls_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='mask_compliance',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'good', b'good'), (b'bad', b'bad')]),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='room_air_changes',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'0.3', b'0.3'), (b'1', b'1'), (b'3', b'3'), (b'10', b'10')]),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='room_volume',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'30m', b'30m'), (b'100m', b'100m'), (b'300m', b'300m'), (b'1000m', b'1000m'), (b'3000m', b'3000m')]),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='task_duration',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='task_frequency',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='task_periodicity',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'day', b'day'), (b'week', b'week'), (b'month', b'month'), (b'year', b'year')]),
        ),
        migrations.DeleteModel(
            name='AsbestosMaterial',
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='local_controls_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.AsbestosLocalControl', null=True),
        ),
    ]
