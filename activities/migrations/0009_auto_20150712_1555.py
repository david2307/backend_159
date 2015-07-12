# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0007_auto_20150711_2332'),
        ('activities', '0008_auto_20150712_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PotentialAttendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('type_vote', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='assitant',
            new_name='count_assistant',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='down_vote',
            new_name='count_down_vote',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='potential_attendee',
            new_name='count_potential_attendee',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='up_vote',
            new_name='count_up_vote',
        ),
        migrations.AddField(
            model_name='vote',
            name='activity',
            field=models.ForeignKey(to='activities.Activity'),
        ),
        migrations.AddField(
            model_name='vote',
            name='person',
            field=models.ForeignKey(to='persons.Person'),
        ),
        migrations.AddField(
            model_name='potentialattendee',
            name='activity',
            field=models.ForeignKey(to='activities.Activity'),
        ),
        migrations.AddField(
            model_name='potentialattendee',
            name='person',
            field=models.ForeignKey(to='persons.Person'),
        ),
        migrations.AddField(
            model_name='assistant',
            name='activity',
            field=models.ForeignKey(to='activities.Activity'),
        ),
        migrations.AddField(
            model_name='assistant',
            name='person',
            field=models.ForeignKey(to='persons.Person'),
        ),
    ]
