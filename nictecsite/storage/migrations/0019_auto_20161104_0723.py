# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0018_remove_equipment_used_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Used_quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_quantity', models.PositiveIntegerField(default=0)),
                ('equipment', models.ManyToManyField(blank=True, to='storage.Equipment')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='equipment_quantity',
            field=models.ManyToManyField(blank=True, to='storage.Used_quantity'),
        ),
    ]
