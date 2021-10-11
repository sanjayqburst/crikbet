from django.urls import path
from ..views import MatchPlayerView


urlpatterns = [
    path('view/',MatchPlayerView.as_view(),name="playerview")
    
]
