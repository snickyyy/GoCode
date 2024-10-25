from django.urls import path

from accounts.views import Profile, UserLogin, UserRegistration

app_name = "students"
urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", UserRegistration.as_view(), name="register"),
    path("profile/", Profile.as_view(), name="profile"),
]
