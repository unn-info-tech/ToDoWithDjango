from django.urls import path
from .views import (
    create,
    read,
    update,
    delete

)

urlpatterns=[
    path("/", create),
    path("list/", read),
    path("mark/", update),
    path("delete/", delete)
]