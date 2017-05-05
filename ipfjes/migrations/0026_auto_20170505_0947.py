# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0025_scarringdrugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scarringdrugs',
            name='amiodarone',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='azathioprine',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='flecainade',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='gefitinib',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='ifosfamide',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='melphalan',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='nitrofurantoin',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='scarringdrugs',
            name='rituximab',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
