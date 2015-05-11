# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150510_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='description',
            field=models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x96\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='container',
            name='weight',
            field=models.IntegerField(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb0\xd0\xb6'),
            preserve_default=True,
        ),
    ]
