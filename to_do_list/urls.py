from django.urls import path
from . import views

urlpatterns=[
    path("createVazifa/", views.createVazifa, name="createVazifa"),
    path("readVazifa/", views.readVazifa),
    path("update/", views.update),
    path("delete/", views.delete),

    path("uquvchilar/", views.listUquvchi),
    path("createUquvchi/", views.createUquvchi, name="createUquvchi"),
]
