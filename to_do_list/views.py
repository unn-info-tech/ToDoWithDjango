from django.http import HttpResponse
from django.shortcuts import render
from .models import Vazifalar
# CRUD

def create(request):
    return HttpResponse("Add a new one")

def read(request): #list of activities
    model = Vazifalar.objects.all().values()
    context = {"nomi": model}
    return render(request, "to_do_list/home.html", context)

def update(request):
    return HttpResponse("Mark your activity")

def delete(request):
    return HttpResponse("Delete you activity")
