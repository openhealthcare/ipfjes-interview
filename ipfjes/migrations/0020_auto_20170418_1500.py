# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0019_auto_20170418_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsbestosExposureHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('percent_task', models.FloatField(null=True, blank=True)),
                ('handling_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('mask_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('asbestos_material_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('task_location_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AsbestosHandling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AsbestosMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BloodRelationHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('age_at_diagnosis', models.IntegerField(null=True, blank=True)),
                ('age_at_death', models.IntegerField(null=True, blank=True)),
                ('relation_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('diagnosis_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_bloodrelationhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('diagnosis_fk', models.ForeignKey(blank=True, to='opal.Condition', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EverEncounteredAsbestos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('contact_with', models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('created_by', models.ForeignKey(related_name='created_ipfjes_everencounteredasbestos_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ipfjes_everencounteredasbestos_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Mask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskLocation',
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
            model_name='diagnosishistory',
            name='initial_consult_reason',
        ),
        migrations.AddField(
            model_name='diagnosishistory',
            name='breathlessness',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='diagnosishistory',
            name='cough',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='diagnosishistory',
            name='incidental',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='diagnosishistory',
            name='incidental_desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diagnosishistory',
            name='other',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyparticipantdetails',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyparticipantdetails',
            name='email_address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='studyparticipantdetails',
            name='postal_address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studyparticipantdetails',
            name='want_updates',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='dyspnoea',
            name='breathless',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='dyspnoea',
            name='dressing_undressing',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='dyspnoea',
            name='short_of_breath',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='dyspnoea',
            name='slower_than_most',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='dyspnoea',
            name='stops_for_breath',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='bloodrelationhistory',
            name='relation_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.Relationship', null=True),
        ),
        migrations.AddField(
            model_name='bloodrelationhistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_ipfjes_bloodrelationhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='asbestos_material_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.AsbestosMaterial', null=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='created_by',
            field=models.ForeignKey(related_name='created_ipfjes_asbestosexposurehistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='episode',
            field=models.ForeignKey(to='opal.Episode'),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='handling_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.AsbestosHandling', null=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='mask_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.Mask', null=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='task_location_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.TaskLocation', null=True),
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_ipfjes_asbestosexposurehistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
