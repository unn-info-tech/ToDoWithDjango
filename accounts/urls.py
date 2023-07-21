from django.urls import path
from . import views

urlpatterns=[
    path("registerFoydalanuvchi/", views.registerFoydalanuvchi, name="registerFoydalanuvchi"),
    path("loginFoydalanuvchi/", views.loginFoydalanuvchi, name="loginFoydalanuvchi"),
    path("logoutFoydalanuvchi/", views.logoutFoydalanuvchi, name="logoutFoydalanuvchi"),

    

]