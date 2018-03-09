# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-01 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network_ui', '0001_squashed_0036_auto_20180223_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='type',
            new_name='device_type',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='type',
            new_name='group_type',
        ),
        migrations.RenameField(
            model_name='process',
            old_name='type',
            new_name='process_type',
        ),
        migrations.AlterField(
            model_name='datasheet',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui.Client'),
        ),
    ]