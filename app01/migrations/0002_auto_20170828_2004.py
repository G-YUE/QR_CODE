# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erweima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Erweima')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='head',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
    ]
