from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import VazifaModel, UquvchiModel
from .forms import VazifaPostForm, UquvchiForm

#=====================================================================================
def detailVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    if request.user.is_authenticated:
        return render(request, "to_do_list/detailVazifa.html", {"objMe": objMe})
    else:
        return redirect("readVazifa")


#=====================================================================================

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
 

def readVazifa(request): #list of activities
    modelMe = VazifaModel.objects.all().values()
    return render(request, "to_do_list/readVazifa.html", {"modelMe": modelMe})

def update(request):
    return HttpResponse("Mark your activity")

def delete(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    objMe.delete()
    return redirect("readVazifa")



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
