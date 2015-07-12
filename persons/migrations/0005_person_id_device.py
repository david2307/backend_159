# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_person_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id_device',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
