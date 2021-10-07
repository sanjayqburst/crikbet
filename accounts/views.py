from django.views.generic.base import  TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as views_auth
from .forms import RegisterUserForm


class LoginView(SuccessMessageMixin,views_auth.LoginView):
    # form_class=LoginForm
    redirect_authenticated_user=True
    success_message = "You were successfully logged in."

    def get_success_url(self):
        # write your logic here
        if self.request.user.is_staff:
            return '/admin'
        return '/home/'


class HomeView(LoginRequiredMixin,TemplateView):
    template_name='home/home.html'



class RegisterView(SuccessMessageMixin,CreateView):
    """
    Method to create new user

    Params:
        CreateView View: Creates view for user registration.
    """
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    form_class = RegisterUserForm    
    success_message = "Your profile was created successfully. Pleapy    se login to continue."

