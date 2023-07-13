from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import VazifaModel, UquvchiModel
from .forms import VazifaPostForm, UquvchiForm
# CRUD

def createVazifa(request):
    if request.method == 'POST':
        formMe =  VazifaPostForm(request.POST)
        if formMe.is_valid():
            formMe.save()
            # do something with the new Odam instance
            return redirect("createVazifa")
    else:
        formMe =  VazifaPostForm()
    return render(request, 'to_do_list/vazifaForm.html', {'formMe': formMe})

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

    
    

def readVazifa(request): #list of activities
    modelMe = VazifaModel.objects.all().values()
    return render(request, "to_do_list/readVazifa.html", {"modelMe": modelMe})

def update(request):
    return HttpResponse("Mark your activity")

def delete(request):
    return HttpResponse("Delete you activity")



#===========================================================================================
def listUquvchi(request):
    modelMe = UquvchiModel.objects.all().values()
    return render(request, "to_do_list/listUquvchi.html", {"modelMe": modelMe})


def createUquvchi(request):
    if request.method == 'POST':
        formMe =  UquvchiForm(request.POST)
        if formMe.is_valid():
            formMe.save()
            # do something with the new Odam instance
            return redirect("createUquvchi")
    else:
        formMe =  UquvchiForm()
    return render(request, 'to_do_list/uquvchiForm.html', {'formMe': formMe})
