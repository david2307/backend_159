# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_person_id_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id_device',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
