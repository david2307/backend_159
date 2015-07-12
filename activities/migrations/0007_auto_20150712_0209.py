# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_activity_potential_attendee'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='assitant',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='down_vote',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='up_vote',
            field=models.IntegerField(null=True),
        ),
    ]
