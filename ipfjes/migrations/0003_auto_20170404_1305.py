# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipfjes', '0002_occupationalhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalhistory',
            name='consistency_token',
            field=models.CharField(default='hello', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='created_by',
            field=models.ForeignKey(related_name='created_ipfjes_occupationalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='patient',
            field=models.ForeignKey(default=1, to='opal.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_ipfjes_occupationalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
