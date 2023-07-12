from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Vazifalar, UquvchiModel
from .forms import VazifaPostForm, UquvchiForm
# CRUD

def create(request):
    if request.method == 'POST':
        formMe =  UquvchiForm(request.POST)
        if formMe.is_valid():
            formMe.save()
            # do something with the new Odam instance
            return redirect("create")
    else:
        formMe =  UquvchiForm()
    return render(request, 'to_do_list/forms.html', {'formMe': formMe})

    """formMe = VazifaPostForm(request.POST or None)
    if formMe.is_valid():
        sar = formMe.cleaned_data("vvvvvvv")
        tul = formMe.cleaned_data("ffffffff")
        save = Vazifalar(sarlavha=sar, tuliq_malumot=tul)
        save.save()
        return redirect("succes")
    else:
        return HttpResponse("did'nt worked")
"""

    
    

def read(request): #list of activities
    modelMe = Vazifalar.objects.all().values()
    context = {"nomi": modelMe}
    return render(request, "to_do_list/home.html", context)

def update(request):
    return HttpResponse("Mark your activity")

def delete(request):
    return HttpResponse("Delete you activity")
    #dkfdjfksdfjalkdf


def uquvchiFunction(request):
    modelMe = UquvchiModel.objects.all().values()
    return render(request, "to_do_list/uquvchi.html", {"modelMe": modelMe})
