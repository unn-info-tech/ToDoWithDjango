from django.urls import path
from . import views

urlpatterns=[
    path("creat/", views.create),
    path("read/", views.read),
    path("update/", views.update),
    path("delete/", views.delete),
    path("check/", views.check)
]
