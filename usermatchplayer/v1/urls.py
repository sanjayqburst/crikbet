from django.urls import path
from ..views import UserMatchPlayerView

urlpatterns = [
    path('view/',UserMatchPlayerView.as_view(),name="usermatchplayerview")
    
]
