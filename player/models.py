from django.db import models
from team.models import Teams

# Create your models here.

class Players(models.Model):
    """
    Model for  player and team assigning.
    """
    player_name=models.CharField(max_length=255,blank=False,null=False)
    team=models.ForeignKey(Teams,on_delete=models.CASCADE,related_name='team_belong')

    def __str__(self):
        return self.player_name +' - '+ self.team.team_name
