from django.db import models
from player.models import Players
from usermatch.models import UserMatches
# Create your models here.


class UserMatchPlayer(models.Model):
    """
    Model for  user matches player selections.
    """
    user_player=models.ForeignKey(Players,on_delete=models.CASCADE,related_name='player_user')
    user_match=models.ForeignKey(UserMatches,on_delete=models.CASCADE,related_name='match_user')
    
    def __str__(self):
        return self.user_player.player_name+" for "+ self.user_match.user_match_id.match_name+" by "+self.user_match.user_id.username