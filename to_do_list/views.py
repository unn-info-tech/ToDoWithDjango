from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import VazifaModel, UquvchiModel
from .forms import VazifaPostForm, UquvchiForm
from django.contrib.auth.forms import UserCreationForm

#=====================================================================================

def readVazifa(request): #list of activities
    modelMe = VazifaModel.objects.all().values()
    return render(request, "to_do_list/readVazifa.html", {"modelMe": modelMe})


# CRU

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
 

def detailVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    if request.user.is_authenticated:
        return render(request, "to_do_list/detailVazifa.html", {"objMe": objMe})
    else:
        return redirect("readVazifa")

def updateVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    if request.method == 'POST':
        formMe =  VazifaPostForm(request.POST, instance=objMe)
        if formMe.is_valid():
            formMe.save()
            # do something with the new Odam instance
            return redirect('detailVazifa', idMe=idMe)
    else:
        formMe =  VazifaPostForm(instance=objMe)
    return render(request, 'to_do_list/vazifaForm.html', {'formMe': formMe})
 
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
#==============================================================================
# User Sign Up, Sign In

def registerFoydalanuvchi(request):
    if request.method == "POST":
        formMe = UserCreationForm(request.POST)
        if formMe.is_valid():
            formMe.save()
            redirect("registerFoydalanuvchi")
    else:
        formMe = UserCreationForm()
    return render(request, 'to_do_list/registerFoydalanuvchi.html', {'formMe': formMe})
    

