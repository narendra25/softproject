# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-02 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtype', models.CharField(max_length=5)),
                ('bankname', models.CharField(max_length=15)),
                ('cardholdername', models.CharField(max_length=10)),
                ('cardnumber', models.IntegerField(default=11)),
                ('cvvno', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='registrationpage',
            fields=[
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=10)),
                ('fathername', models.CharField(max_length=10)),
                ('cno', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ticketbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromplace', models.CharField(max_length=10)),
                ('toplace', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('journeydate', models.DateField()),
                ('searchtrain', models.CharField(max_length=10)),
            ],
        ),
    ]
