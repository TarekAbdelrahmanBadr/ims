# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-07 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0002_auto_20170802_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ansbe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inst', models.CharField(max_length=10)),
                ('OS', models.CharField(max_length=6)),
                ('Roles', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='ansb',
            old_name='IP',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='ansb',
            old_name='ver',
            new_name='Instance',
        ),
        migrations.RenameField(
            model_name='ansb',
            old_name='role',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='ansb',
            name='key_name',
            field=models.CharField(default=False, max_length=15),
            preserve_default=False,
        ),
    ]
