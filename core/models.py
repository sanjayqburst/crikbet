from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum

# Create your models here.

class Teams(models.Model):
    """
    Model for  Teams.
    """
    team_name=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.team_name


class Players(models.Model):
    """
    Model for  player and team assigning.
    """
    player_name=models.CharField(max_length=255,blank=False,null=False)
    team=models.ForeignKey(Teams,on_delete=models.CASCADE,related_name='team_belong')

    def __str__(self):
        return self.player_name +' - '+ self.team.team_name


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


class MatchPlayer(models.Model):
    """
    Model for  match player selections.
    """
    player_id=models.ForeignKey(Players,on_delete=models.CASCADE,related_name='id_player')
    match_id=models.ForeignKey(Matches,on_delete=models.CASCADE,related_name='id_match')
    points=models.IntegerField()

    def __str__(self):
        return 'score of '+self.player_id.player_name+' for the '+self.match_id.match_name+' is '+ str(self.points)


class UserMatches(models.Model):
    """
    Model for  user match selections.
    """
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='id_user')
    user_match_id=models.ForeignKey(Matches,on_delete=models.CASCADE,related_name="id_user_match")

    def __str__(self):
        return "Joined by "+self.user_id.username+' for '+self.user_match_id.match_name


class UserMatchPlayer(models.Model):
    """
    Model for  user matches player selections.
    """
    user_player=models.ForeignKey(Players,on_delete=models.CASCADE,related_name='player_user')
    user_match=models.ForeignKey(UserMatches,on_delete=models.CASCADE,related_name='match_user')

    def __str__(self):
        return self.user_player.player_name+" for "+ self.user_match.user_match_id.match_name+" by "+self.user_match.user_id.username