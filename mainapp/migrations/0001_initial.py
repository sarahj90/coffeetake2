# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-03 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('espresso_shots', models.PositiveIntegerField(default=1)),
                ('water', models.FloatField(default=0)),
                ('steamed_milk', models.BooleanField(default=False)),
                ('foam', models.FloatField(default=0)),
                ('extra_instructions', models.TextField()),
                ('bean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Bean')),
            ],
        ),
        migrations.CreateModel(
            name='Powder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Roast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Syrup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(to='mainapp.Powder'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='roast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Roast'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(to='mainapp.Syrup'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
