from django.urls import path 
from .views import *

urlpatterns = [
    path("login/", Loginview, name="login"),
    path("register/", register, name="register"),
    path("forgot-password/", forgot_password, name="forgot-password"),
    path("otp-validation/", otp_validation, name="otp-validation"),
    path("password-reset/", password_reset, name="password-reset"),
    path("home/", home, name="home"),
]