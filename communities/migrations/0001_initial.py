# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_person_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('purpose', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('logo', models.ImageField(null=True, upload_to=b'')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CommunityRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('community', models.ForeignKey(to='communities.Community')),
                ('person', models.ForeignKey(to='persons.Person')),
                ('role', models.ForeignKey(to='communities.CommunityRole')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('community', models.ForeignKey(to='communities.Community')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=300)),
                ('community', models.ForeignKey(to='communities.Community')),
            ],
        ),
        migrations.CreateModel(
            name='TypeSocialNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='type_social',
            field=models.ForeignKey(to='communities.TypeSocialNetwork'),
        ),
        migrations.AddField(
            model_name='community',
            name='sector',
            field=models.ForeignKey(to='communities.Sector'),
        ),
    ]
