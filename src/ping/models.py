from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)

class Match(models.Model):
    score = models.CharField(max_length=200)
    played_at = models.DateTimeField('date published')
    player1 = models.ForeignKey(Player, related_name='match_set_p1')
    player2 = models.ForeignKey(Player, related_name='match_set_p2')
