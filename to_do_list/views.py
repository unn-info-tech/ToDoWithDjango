from django.http import HttpResponse
from django.shortcuts import render
from .models import Vazifalar
from .forms import TodoPostForm
# CRUD

def create(request):
    formMe = TodoPostForm(request.POST or None)
    if formMe.is_valid():
        print("it's working", formMe.cleaned_data)
        obj = formMe.save(commit=False)
        obj.save()
        formMe = TodoPostForm()
    contextMe = {"obj": formMe}
    return render(request, "to_do_list/forms.html", contextMe)
    

def read(request): #list of activities
    modelMe = Vazifalar.objects.all().values()
    context = {"nomi": modelMe}
    return render(request, "to_do_list/home.html", context)

def update(request):
    return HttpResponse("Mark your activity")

def delete(request):
    return HttpResponse("Delete you activity")
    #dkfdjfksdfjalkdf


def check(request):
    return render(request, "to_do_list/base.html")
