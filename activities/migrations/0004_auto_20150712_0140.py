# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activity_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True),
        ),
    ]
