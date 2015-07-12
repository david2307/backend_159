# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'communities'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='community',
            field=models.ForeignKey(related_name='objectives', to='communities.Community'),
        ),
    ]
