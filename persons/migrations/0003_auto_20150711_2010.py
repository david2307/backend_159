# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_person_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='confirmation',
            field=models.NullBooleanField(),
        ),
    ]
