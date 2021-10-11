from django.urls import path

from player.views import PlayerView

urlpatterns = [
    path('view/',PlayerView.as_view(),name="playerview")
]
