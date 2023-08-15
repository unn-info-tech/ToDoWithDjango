from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, datetime, timedelta
from itertools import groupby
from operator import itemgetter
import json




from django.contrib.admin.views.decorators import staff_member_required
from .models import VazifaModel, DateBajarildiModel
from .forms import VazifaPostForm






#=====================================================================================
@login_required
def readVazifa(request): #list of activities
    # __gt = Filter the to-do items where the due date is greater than the current datetime
    print(timezone.localdate().year)
    modelMe = VazifaModel.objects.filter(
        tugatish_muddati__gt=timezone.localtime().time(),
        bajarilgan_date__date__gte=timezone.localdate().strftime('%Y-%m-%d'),
        foydalanuvchi=request.user,
        bajarildi=False).order_by('bajarilgan_date__date', 'boshlanish_vaqti')
    

    # Create a list to store the grouped to-do items and date headings
    dateMe = timezone.localdate()
    grouped_items = []
    for date, vazifalar in groupby(modelMe, key=lambda x: x.bajarilgan_date):
        boo = f'{dateMe}' == f'{date}'
        print(boo)
        grouped_items.append({
            'vazifa_kuni': date,
            'vazifalar': sorted(vazifalar, key=lambda vazifa: vazifa.boshlanish_vaqti),
            'dat': boo,
        })
        

    return render(request, "to_do_list/readVazifa.html", {"modelMe": grouped_items, 
                                                          'timeMe': timezone.localtime().time(),
                                                          'dateMe': timezone.localdate().strftime('%Y-%m-%d'),
                                                          })

#=================================================================================
# CRDU

@login_required
def createVazifa(request):
    if request.method == 'POST':
        formMe =  VazifaPostForm(request.POST)
        if formMe.is_valid():
            input_date = formMe.cleaned_data['input_date']
            challenge = int(formMe.cleaned_data['challenge'])
            vazifas = []
            for i in range(challenge):
                vazifa_kuni, created = DateBajarildiModel.objects.get_or_create(date=input_date + timedelta(days=i), foydalanuvchi=request.user)
                vazifa = VazifaModel(
                    foydalanuvchi = request.user,
                    sarlavha=formMe.cleaned_data['sarlavha'],
                    tuliq_malumot=formMe.cleaned_data['tuliq_malumot'],
                    bajarilgan_date = vazifa_kuni,
                    boshlanish_vaqti=formMe.cleaned_data['boshlanish_vaqti'],
                    tugatish_muddati=formMe.cleaned_data['tugatish_muddati'],
                )
                vazifas.append(vazifa)
                
            VazifaModel.objects.bulk_create(vazifas)
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
            return redirect('readVazifa')
                
            
    else:
        formMe =  VazifaPostForm(instance=objVazifa)
    return render(request, 'to_do_list/updateVazifa.html', {'formMe': formMe})

@login_required 
def deleteVazifa(request, idMe):
    objMe = get_object_or_404(VazifaModel, id=idMe)
    objMe.delete()
    return redirect("readVazifa")

#===========================

# History request
def historyVazifa(request):
    date_now = timezone.localdate()
    modelMe = DateBajarildiModel.objects.filter(
        date__lte = date_now,
        foydalanuvchi=request.user,
    ).values() # historyVazifalar

    last_10kun = date_now - timezone.timedelta(days=10)
    # Delete older records for non-staff users
    if not request.user.is_staff:
        DateBajarildiModel.objects.filter(
            date__lt=last_10kun,
            foydalanuvchi=request.user
        ).delete()
    dat = []
    for item in modelMe:
        item['date'] = item['date'].strftime("%Y-%m-%d")
        dat.append(item)
    return render(request, "to_do_list/historyVazifa.html", {"modelMe": dat})


# delete History Date
def historyDeleteDate(request, idMe):
    objMe = get_object_or_404(DateBajarildiModel, id=idMe)
    objMe.delete()
    return redirect("historyVazifa")

# time difference without request
def calculate_time_difference(boshlanish_vaqti, bajarilgan_vaqt):
    boshlanish_vaqti = datetime.combine(timezone.localdate(), boshlanish_vaqti)
    bajarilgan_vaqt = datetime.combine(timezone.localdate(), bajarilgan_vaqt)
    time_difference = bajarilgan_vaqt - boshlanish_vaqti
    print("TIME DIFFERENCE:",time_difference)
    total_hours = time_difference.total_seconds() // 3600  # Calculate total hours
    total_minutes = (time_difference.total_seconds() % 3600) / 60  # Calculate remaining minutes

    total_decimal = total_hours + (total_minutes / 60)  # Convert minutes to decimal part

    return total_decimal

# progress
def progress(request):
    date_now = timezone.localdate()
    kunlar = DateBajarildiModel.objects.filter(
        date__lte = date_now,
        foydalanuvchi=request.user,
    ) # historyVazifalar
    last_10kun = date_now - timezone.timedelta(days=10)
    # Delete older records for non-staff users
    if not request.user.is_staff:
        DateBajarildiModel.objects.filter(
            date__lt=last_10kun,
            foydalanuvchi=request.user
        ).delete()

    print(kunlar)
    bajarilgan_by_date = {}
    vazifalar = []
    for record in kunlar:
        suralgan_date = record
        print(suralgan_date, "suralgan122")

        vazifalar = VazifaModel.objects.filter(
            bajarilgan_date=suralgan_date,
            foydalanuvchi=request.user,
            bajarildi=True
        ).values()
        print(vazifalar)
        
        converted_queryset = []
        for object in vazifalar:
            print('bajarildi:',object['bajarildi'])
            boshlanish_vaqti_str = object['boshlanish_vaqti']
            bajarilgan_vaqt_str = object['bajarilgan_vaqt']
            print("Boshlanish vaqti:", boshlanish_vaqti_str)
            print("Bajarilgan vaqt:", bajarilgan_vaqt_str)

            float = calculate_time_difference( boshlanish_vaqti_str, bajarilgan_vaqt_str)
            print("float:",float)
            converted_queryset.append(float)
            print(converted_queryset)
         

        bajarilgan_by_date[suralgan_date.date.strftime('%Y-%m-%d')] = sum(converted_queryset)
    print(bajarilgan_by_date)
    data_json = json.dumps(bajarilgan_by_date)
    print(data_json)
    
    return render(request, "to_do_list/progress.html", {'data_json': data_json})






#==========================================================
# Done and Undone
@login_required
def bajarilganVazifalar(request, idMe):
    suralgan_date = get_object_or_404(DateBajarildiModel, id=idMe)
    bajarilgan = VazifaModel.objects.filter(
        bajarilgan_date=suralgan_date, 
        foydalanuvchi=request.user, 
        bajarildi=True).values()
    return render(request, "to_do_list/filteredHistoryVazifalar.html", {"bajarilgan": bajarilgan,
                                                                        'idMe': idMe,
                                                                        'len_bajarilgan': len(bajarilgan),
                                                                        'suralgan_date': suralgan_date})
                                                                        
    
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
    objVazifa.bajarilgan_date, created = DateBajarildiModel.objects.get_or_create(date=timezone.localdate(),
                                                                                  foydalanuvchi=request.user,)
    objVazifa.save()
    return redirect('readVazifa')    


#===========================================================================================

# Functions without request

    




