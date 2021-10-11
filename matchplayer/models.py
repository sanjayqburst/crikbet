from django.db import models
from match.models import Matches
from player.models import Players
# Create your models here.

class MatchPlayer(models.Model):
    """
    Model for  match player selections.
    """
    player_id=models.ForeignKey(Players,on_delete=models.CASCADE,related_name='id_player')
    match_id=models.ForeignKey(Matches,on_delete=models.CASCADE,related_name='id_match')
    points=models.IntegerField()

    def __str__(self):
        return 'Point of '+self.player_id.player_name+' for the '+self.match_id.match_name+' is '+ str(self.points)
