# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machinelearning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo_code', models.CharField(max_length=10)),
                ('algo_name', models.CharField(max_length=100)),
            ],
        ),
    ]
