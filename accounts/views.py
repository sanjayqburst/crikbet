from django.http.request import HttpHeaders, HttpRequest
from django.views.generic.base import  TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as views_auth
import datetime
from match.models import Matches
from matchplayer.models import MatchPlayer
from player.models import Players
from usermatch.models import UserMatches
from usermatchplayer.models import UserMatchPlayer
from .forms import RegisterUserForm


class LoginView(SuccessMessageMixin,views_auth.LoginView):
    """
    View class for handling Login request:
    """
    redirect_authenticated_user=True
    success_message = "You were successfully logged in."

    def get_success_url(self):
        # write your logic here
        if self.request.user.is_staff:
            return '/admin'
        return '/'


class HomeView(LoginRequiredMixin,TemplateView):
    """
    View for rendering home page for users.
    """
    matches=Matches.objects
    time_now=datetime.datetime.now()
    match_with_time=Matches.objects.filter(match_time__gte=time_now)
    user_match=UserMatches.objects
    match_show=Matches.objects.filter(match_time__lte=time_now)
    points=MatchPlayer.objects
    extra_context={'matches':matches,'user_matches':user_match,'time_now':match_with_time,'match_over':match_show}
    template_name='home/home.html'


class AddTeamView(LoginRequiredMixin,CreateView):
    """
    View for Joining new match by user. 
    """
    template_name='addteam/addteam.html'
    model=UserMatchPlayer
    fields='__all__'
    # lookup_url_kwarg='match_id'
    usermatch=UserMatches.objects
    player=Players.objects
    matches=Matches.objects
    extra_context={'players':player,'matches':matches,'usermatch':usermatch}
    

    
    

class RegisterView(SuccessMessageMixin,CreateView):
    """
    Method to create new user
    """
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    form_class = RegisterUserForm    
    success_message = "Your profile was created successfully. Pleapy    se login to continue."

class SelectPlayerView(SuccessMessageMixin,CreateView):
    """
    Method for selecting players for user 
    """
    matches=Matches.objects
    player=Players.objects
    usermatch=UserMatches.objects
    model=UserMatchPlayer
    fields='__all__'
    extra_context={'players':player,'matches':matches,"usermatch":usermatch}
    template_name='selectplayer/selectplayer.html'
    success_url=reverse_lazy('home')