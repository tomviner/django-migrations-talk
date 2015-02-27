# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0002_auto_20150227_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='score',
            field=models.CharField(max_length=200, verbose_name=b'Score'),
        ),
    ]
