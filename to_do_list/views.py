from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.contrib.admin.views.decorators import staff_member_required
from .models import VazifaModel, UquvchiModel, BajarildiModel
from .forms import VazifaPostForm, UquvchiForm






#=====================================================================================
@login_required
def readVazifa(request): #list of activities
    modelMe = VazifaModel.objects.filter(foydalanuvchi=request.user).values()
    return render(request, "to_do_list/readVazifa.html", {"modelMe": modelMe})

#=================================================================================
# CRDU

@login_required
def createVazifa(request):
    if request.method == 'POST':
        formMe =  VazifaPostForm(request.POST)
        if formMe.is_valid():
            vazifa = formMe.save(commit=False)
            vazifa.foydalanuvchi = request.user
            formMe.save()

            return redirect("readVazifa")
    else:
        formMe =  VazifaPostForm()
    return render(request, 'to_do_list/createVazifa.html', {'formMe': formMe})
 
@login_required
def detailVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    if request.user.is_authenticated:
        return render(request, "to_do_list/detailVazifa.html", {"objMe": objMe})
    else:
        return redirect("readVazifa")

@login_required
def updateVazifa(request, idMe):
    objVazifa = get_object_or_404(VazifaModel, id=idMe)
    if request.method == 'POST':
        formMe =  VazifaPostForm(request.POST, instance=objVazifa)
        if formMe.is_valid():
            formMe.save()
            if objVazifa.bajarildi:
                bajarildiVazifa(request, objVazifa)
            return redirect('readVazifa')
                
            
    else:
        formMe =  VazifaPostForm(instance=objVazifa)
    return render(request, 'to_do_list/updatesimple.html', {'formMe': formMe})

@login_required 
def deleteVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    objMe.delete()
    return redirect("readVazifa")

#===========================

def bajarildiVazifa(request, objVazifa):
    BajarildiModel.objects.create(
        sarlavha = objVazifa.sarlavha,
        tuliq_malumot = objVazifa.tuliq_malumot,
        tugatilgan_muddat = timezone.now(),
    )
    
    objVazifa.delete()
    
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


    

