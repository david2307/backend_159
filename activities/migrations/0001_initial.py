# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_auto_20150711_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('begin_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('latitude', models.DecimalField(null=True, max_digits=23, decimal_places=20)),
                ('longitude', models.DecimalField(null=True, max_digits=23, decimal_places=20)),
                ('minimum_assitant', models.IntegerField()),
                ('town', models.ForeignKey(to='persons.Town')),
            ],
        ),
    ]
