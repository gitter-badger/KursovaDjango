# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='container',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='distinct',
            options={'ordering': ['-id'], 'verbose_name': '\u0420\u0430\u0439\u043e\u043d'},
        ),
        migrations.AlterModelOptions(
            name='marchent',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='container',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 5, 10, 19, 38, 6, 25108, tzinfo=utc), max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='distinct',
            name='name',
            field=models.CharField(unique=True, max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marchent',
            name='description',
            field=models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marchent',
            name='last_name',
            field=models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd0\xbe-\xd0\x91\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marchent',
            name='sur_name',
            field=models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='owner',
            name='description',
            field=models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='owner',
            name='last_name',
            field=models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd0\xbe-\xd0\x91\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='owner',
            name='sur_name',
            field=models.CharField(max_length=70, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5'),
            preserve_default=True,
        ),
    ]
