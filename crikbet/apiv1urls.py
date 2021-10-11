from django.urls import path,include
urlpatterns = [
    path('team/',include('team.v1.urls'),name='teamv1'),
    path('player/',include('player.v1.urls'),name='playerv1'),
    path('match/',include('match.v1.urls'),name='matchv1'),
    path('matchplayer/',include('matchplayer.v1.urls'),name='matchplayerv1'),
    path('usermatch/',include('usermatch.v1.urls'),name='usermatchv1'),
    path('usermatchplayer/',include('usermatchplayer.v1.urls'),name='usermatchplayerv1'),
]
