from django.urls import path ,re_path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('join/',views.AddTeamView.as_view(),name='join'),
    # re_path(r'^join/id=(?P<match_id>\d+)/$',views.AddTeamView.as_view(),name='join'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('register/', views.RegisterView.as_view(),name='register'),
]
