# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 18:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opqpwd', '0009_auto_20161115_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encpasslist', models.TextField(max_length=266924, validators=[django.core.validators.RegexValidator(message='Expecting Base64 string', regex='^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'), django.core.validators.RegexValidator(message='length has to be 266924', regex='^.{266924}$')])),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passworddata', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='password',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Password',
        ),
    ]