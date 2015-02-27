from django.db import models


class Match(models.Model):
    score = models.CharField(max_length=200, verbose_name='Score')
    weather = models.CharField(max_length=200, null=True)
    games = models.IntegerField(null=True)
    played_at = models.DateTimeField('date published')
    player1 = models.ForeignKey('human.Player', related_name='match_set_p1', null=True)
    player2 = models.ForeignKey('human.Player', related_name='match_set_p2', null=True)
