from django.urls import path
from . import views

urlpatterns=[
    path("createVazifa/", views.createVazifa, name="createVazifa"),
    path("readVazifa/", views.readVazifa, name="readVazifa"),
    path("update/", views.update),
    path("readVazifa/<int:idMe>/delete/", views.delete),

    path("readVazifa/<int:idMe>/", views.detailVazifa),

    path("uquvchilar/", views.listUquvchi),
    path("createUquvchi/", views.createUquvchi, name="createUquvchi"),
]
