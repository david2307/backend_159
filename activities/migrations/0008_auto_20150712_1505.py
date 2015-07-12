# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20150712_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='minimum_assitant',
            new_name='minimum_assistant',
        ),
    ]
