from django.urls import path
from . import views

urlpatterns=[
    path("", views.readVazifa, name="readVazifa"),
    path("<int:idMe>/", views.detailVazifa, name="detailVazifa"),
    path("<int:idMe>/update/", views.updateVazifa),
    path("<int:idMe>/delete/", views.delete),

    #==========================================

    path("uquvchilar/", views.listUquvchi),
    path("createUquvchi/", views.createUquvchi, name="createUquvchi"),
]
