from django.urls import path
from . import views

urlpatterns=[
    path("createVazifa/", views.createVazifa, name="createVazifa"),
    path("readVazifa/", views.readVazifa, name="readVazifa"),
    path("readVazifa/<int:idMe>/", views.detailVazifa, name="detailVazifa"),
    path("readVazifa/<int:idMe>/update/", views.updateVazifa, name='updateVazifa'),
    path("readVazifa/<int:idMe>/delete/", views.deleteVazifa, name='deleteVazifa'),
    
    path("historyVazifa/", views.historyVazifa, name='historyVazifa'),
    path("historyDeleteDate/<int:idMe>/", views.historyDeleteDate, name='historyDeleteDate'),
    path("progress/", views.progress, name='progress'),


    path("bajarilganVazifalar/<int:idMe>/", views.bajarilganVazifalar, name='bajarilganVazifalar'),
    path("unBajarilganVazifalar/<int:idMe>/", views.unBajarilganVazifalar, name='unBajarilganVazifalar'),
    
    path("readVazifa/<int:idMe>/bajarildiVazifa/", views.bajarildiVazifa, name='bajarildiVazifa'),

    
    
    




    #==========================================

 


    #==========================================
]
