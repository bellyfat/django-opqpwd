# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opqpwd', '0006_auto_20161111_1400'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UidSet',
            new_name='Password',
        ),
        migrations.DeleteModel(
            name='PasswordData',
        ),
        migrations.RenameField(
            model_name='password',
            old_name='encuidset',
            new_name='encpasslist',
        ),
    ]
