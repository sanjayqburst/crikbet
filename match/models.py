from django.db import models
from team.models import Teams
# Create your models here.

class Matches(models.Model):
    """
    Model for  matches team and time selection.
    """
    match_name=models.CharField(max_length=255,blank=False,null=False)
    home_team=models.ForeignKey(Teams,on_delete=models.CASCADE,related_name='team_home')
    away_team=models.ForeignKey(Teams,on_delete=models.CASCADE,related_name='team_away')
    match_time=models.DateTimeField()

    def __str__(self):
        return self.match_name +" - "+self.home_team.team_name+" vs "+self.away_team.team_name +" on "+str(self.match_time)
