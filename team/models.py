from django.db import models

# Create your models here.

class Teams(models.Model):
    """
    Model for  Teams.
    """
    team_name=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.team_name