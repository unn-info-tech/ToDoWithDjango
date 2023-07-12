from django.urls import path
from . import views

urlpatterns=[
    path("create/", views.create, name="create"),
    path("read/", views.read),
    path("update/", views.update),
    path("delete/", views.delete),
    path("uquvchilar/", views.uquvchiFunction),
]
