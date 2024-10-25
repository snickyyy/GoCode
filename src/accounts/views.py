from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

# Create your views here.


class UserLogin(LoginView):
    template_name = "login.html"


class UserRegistration(CreateView):
    model = get_user_model()
    fields = ["email", "password", "username"]
    template_name = "registration.html"
    success_url = reverse_lazy("index")


class Profile(TemplateView):
    template_name = "profile.html"
