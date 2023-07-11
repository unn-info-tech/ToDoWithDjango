from django.http import HttpResponse
from django.shortcuts import render
from .models import Vazifalar
from .forms import TodoPostForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
# CRUD

def create(request):
    if request.method == 'POST':
        formMe = TodoPostForm(request.POST)
        if formMe.is_valid():
            obj = formMe.save(commit=False)
            obj.save()
            return redirect('todo_list')
    else:
        formMe = TodoPostForm()
    return render(request, 'to_do_list/create.html', {'form': formMe})


    """form = ContactForm(request.POST or None)
    if form.is_valid():
        print("The name of data===================",form.cleaned_data)
        form = ContactForm()
    contact = "Something of mine 'CONTACT'"
    context = {
        "title": contact,
        "form": form
    }
    return render(request, "form.html",context)"""
    

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
