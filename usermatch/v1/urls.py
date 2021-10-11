from django.urls import path
from ..views import UserMatchView

urlpatterns = [
    path('view/',UserMatchView.as_view(),name="usermatchview")
    
]
