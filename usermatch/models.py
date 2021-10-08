from django.db import models
from django.contrib.auth.models import User
from match.models import Matches
# Create your models here.


class UserMatches(models.Model):
    """
    Model for  user match selections.
    """
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='id_user')
    user_match_id=models.ForeignKey(Matches,on_delete=models.CASCADE,related_name="id_user_match")

    def __str__(self):
        return "Joined by "+self.user_id.username+' for '+self.user_match_id.match_name

