# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
                ('weight', models.IntegerField(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb0\xd0\xb6')),
                ('row', models.IntegerField(verbose_name=b'\xd0\xa0\xd1\x8f\xd0\xb4')),
                ('rent', models.CharField(max_length=255, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb0')),
                ('contract_begin', models.DateField(verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xbe\xd0\xba \xd0\xbe\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb8')),
                ('contract_end', models.DateField(verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbd\xd0\xb5\xd1\x86\xd1\x8c \xd0\xbe\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb8')),
                ('description', models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f', blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Distinct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0420\u0430\u0439\u043e\u043d',
            },
        ),
        migrations.CreateModel(
            name='Marchent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=70, verbose_name=b'\xd0\x86\xd0\xbc`\xd1\x8f')),
                ('last_name', models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd0\xbe-\xd0\x91\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96')),
                ('sur_name', models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5')),
                ('telephone', models.CharField(max_length=60, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('email', models.EmailField(max_length=150, verbose_name=b'Email')),
                ('address', models.CharField(max_length=150, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('description', models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f', blank=True)),
                ('city', models.ForeignKey(verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x82\xd0\xbe', to='core.City')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=70, verbose_name=b'\xd0\x86\xd0\xbc`\xd1\x8f')),
                ('last_name', models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd0\xbe-\xd0\x91\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96')),
                ('sur_name', models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5')),
                ('telephone', models.CharField(max_length=60, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('email', models.EmailField(max_length=150, verbose_name=b'Email')),
                ('address', models.CharField(max_length=150, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('description', models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f', blank=True)),
                ('city', models.ForeignKey(verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x82\xd0\xbe', to='core.City')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
                ('city', models.ForeignKey(verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x82\xd0\xbe', to='core.City')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='distinct',
            name='region',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb3\xd1\x96\xd0\xbe\xd0\xbd', to='core.Region'),
        ),
        migrations.AddField(
            model_name='container',
            name='marchent',
            field=models.ForeignKey(verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x80\xd1\x8c', to='core.Marchent'),
        ),
        migrations.AddField(
            model_name='container',
            name='owner',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd1\x81\xd0\xbd\xd0\xb8\xd0\xba', to='core.Owner'),
        ),
        migrations.AddField(
            model_name='container',
            name='place',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd1\x96\xd1\x81\xd1\x86\xd0\xb5', to='core.Place'),
        ),
        migrations.AddField(
            model_name='container',
            name='type',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', to='core.Type'),
        ),
        migrations.AddField(
            model_name='city',
            name='distinct',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd', to='core.Distinct'),
        ),
    ]
