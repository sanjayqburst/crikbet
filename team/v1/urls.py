from django.urls import path,include
from ..views import TeamView
urlpatterns = [
    path('view/',TeamView.as_view(),name='teamview')
]
