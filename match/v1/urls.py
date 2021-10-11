from django.urls import path

from match.views import MatchView

urlpatterns = [
    path('view/',MatchView.as_view(),name="playerview")
]
