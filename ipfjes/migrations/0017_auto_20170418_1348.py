# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0016_smokinghistory_smoking_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smokables',
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
            model_name='smokinghistory',
            name='what_do_you_smoke',
        ),
        migrations.AddField(
            model_name='smokinghistory',
            name='what_do_you_smoke_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='smokinghistory',
            name='what_do_you_smoke_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.Smokables', null=True),
        ),
    ]
