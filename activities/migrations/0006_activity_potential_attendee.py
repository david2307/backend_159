# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20150712_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='potential_attendee',
            field=models.IntegerField(null=True),
        ),
    ]
