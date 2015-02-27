# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0001_initial'),
        ('ping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(null=True, related_name='match_set_p1', to='human.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(null=True, related_name='match_set_p2', to='human.Player'),
        ),
    ]
