from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns=[
    path("deleteFoydalanuvchi/", views.deleteFoydalanuvchi, name="deleteFoydalanuvchi"),
    path("changeParolFoydalanuvchi/", views.changeParolFoydalanuvchi, name="changeParolFoydalanuvchi"),
    path('changeParolFoydalanuvchi/changeParolDone/', PasswordChangeDoneView.as_view(template_name='accounts/changeParolDone.html'), name='changeParolDone'),
    path('changeProfile', views.changeProfile, name="changeProfile"),
    path("editFoydalanuvchi/<int:idMe/", views.editFoydalanuvchi, name="editFoydalanuvchi"),
    path("profileFoydalanuvchi/", views.profileFoydalanuvchi, name="profileFoydalanuvchi"),
    path("registerFoydalanuvchi/", views.registerFoydalanuvchi, name="registerFoydalanuvchi"),
    path("loginFoydalanuvchi/", views.loginFoydalanuvchi, name="loginFoydalanuvchi"),
    path("logoutFoydalanuvchi/", views.logoutFoydalanuvchi, name="logoutFoydalanuvchi"),
    
]