from django.urls import path
from . import views

urlpatterns=[
    path("createVazifa/", views.createVazifa, name="createVazifa"),
    path("readVazifa/<int:idMe>/done", views.bajarildiVazifa, name="bajarildiVazifa"),
    path("readVazifa/", views.readVazifa, name="readVazifa"),
    path("readVazifa/<int:idMe>/", views.detailVazifa, name="detailVazifa"),
    path("readVazifa/<int:idMe>/update/", views.updateVazifa, name='updateVazifa'),
    path("readVazifa/<int:idMe>/delete/", views.deleteVazifa, name='deleteVazifa'),

    #==========================================

 


    #==========================================
]
