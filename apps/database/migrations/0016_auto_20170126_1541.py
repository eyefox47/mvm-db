# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20170124_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('trainee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='database.Trainee')),
            ],
            options={
                'abstract': False,
            },
            bases=('apps.database.trainee',),
        ),
        migrations.AlterModelOptions(
            name='pokemon',
            options={'ordering': ['name'], 'verbose_name': 'Pokémon', 'verbose_name_plural': 'Pokémon'},
        ),
    ]
