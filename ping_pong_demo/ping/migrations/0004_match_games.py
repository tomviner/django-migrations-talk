# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0003_auto_20150227_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='games',
            field=models.IntegerField(null=True),
        ),
    ]
