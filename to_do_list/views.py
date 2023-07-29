from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import pytz
from datetime import date, datetime
from django.db.models import Q




from django.contrib.admin.views.decorators import staff_member_required
from .models import VazifaModel, DateBajarildiModel
from .forms import VazifaPostForm






#=====================================================================================
@login_required
def readVazifa(request): #list of activities
    # __gt = Filter the to-do items where the due date is greater than the current datetime
    print(timezone.localdate())
    modelMe = VazifaModel.objects.filter(
        tugatish_muddati__gt=timezone.localtime().time(),
        bajarilgan_date__date__gte=timezone.localdate(),
        foydalanuvchi=request.user,
        bajarildi=False).values()

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
            input_date = formMe.cleaned_data['input_date']
            vazifa.bajarilgan_date, created = DateBajarildiModel.objects.get_or_create(date=input_date)
            formMe.save()

            return redirect("readVazifa")
    else:
        formMe =  VazifaPostForm()
    return render(request, 'to_do_list/createVazifa.html', {'formMe': formMe})
 
@login_required
def detailVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    print(objMe.bajarilgan_date)
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
            return redirect('detailVazifa', idMe=idMe)
                
            
    else:
        formMe =  VazifaPostForm(instance=objVazifa)
    return render(request, 'to_do_list/updateVazifa.html', {'formMe': formMe})

@login_required 
def deleteVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    objMe.delete()
    return redirect("readVazifa")

#===========================
# History 

def historyVazifa(request):
    modelMe = DateBajarildiModel.objects.all().values() # historyVazifalar
    return render(request, "to_do_list/historyVazifa.html", {"modelMe": modelMe})



#==========================================================
# Done and Undone

def bajarilganVazifalar(request, idMe):
    suralgan_date = get_object_or_404(DateBajarildiModel, id=idMe)
    bajarilgan = VazifaModel.objects.filter(
        bajarilgan_date=suralgan_date, 
        foydalanuvchi=request.user, 
        bajarildi=True).values()
    return render(request, "to_do_list/filteredHistoryVazifalar.html", {"bajarilgan": bajarilgan, 'idMe': idMe, 'len_bajarilgan': len(bajarilgan)})
    
# __lte = Filter the to-do items where the due date is before or equal to the current datetime
@login_required
def unBajarilganVazifalar(request, idMe):
    suralgan_date = get_object_or_404(DateBajarildiModel, id=idMe)
    unBajarilgan = VazifaModel.objects.filter(
        tugatish_muddati__lte=timezone.localtime().time(),
        bajarilgan_date__date__lte=timezone.localdate(),
        bajarilgan_date=suralgan_date, 
        foydalanuvchi=request.user, 
        bajarildi=False).values()
    return render(request, "to_do_list/filteredHistoryVazifalar.html", {"unBajarilgan": unBajarilgan, 'idMe': idMe, 'len_unBajarilgan': len(unBajarilgan)})


# =============================
# Mark the Vazifa done

def bajarildiVazifa(request, idMe):
    objVazifa = get_object_or_404(VazifaModel, id=idMe)
    objVazifa.bajarildi = True
    objVazifa.bajarilgan_vaqt = timezone.localtime().time()
    objVazifa.bajarilgan_date, created = DateBajarildiModel.objects.get_or_create(date=date.today())
    objVazifa.save()
    return redirect('readVazifa')    


#===========================================================================================




