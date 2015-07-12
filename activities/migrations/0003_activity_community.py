# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20150712_0044'),
        ('activities', '0002_activity_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='community',
            field=models.ForeignKey(default=1, to='communities.Community'),
            preserve_default=False,
        ),
    ]
