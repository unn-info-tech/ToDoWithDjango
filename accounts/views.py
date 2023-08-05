from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import sozlangUserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import sozlangUserCreationForm, sozlangUserChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages


# Create your views here.



# User Sign Up, Sign In

def registerFoydalanuvchi(request):
    if request.method == "POST":
        formMe = sozlangUserCreationForm(request.POST)
        if formMe.is_valid():
            # foydalanuvchi = formMe.save(commit=False)
            # foydalanuvchi.is_staff = True
            formMe.save()
            redirect("readVazifa")
    else:
        formMe = sozlangUserCreationForm()
    return render(request, 'accounts/registerFoydalanuvchi.html', {'formMe': formMe})


def loginFoydalanuvchi(request):
    if request.method == "POST":
        formMe = AuthenticationForm(request, data=request.POST)
        if formMe.is_valid():
            ism = formMe.cleaned_data.get('username')
            parol = formMe.cleaned_data.get('password')
            foydalanuvchi = authenticate(request, username=ism, password=parol)
            if foydalanuvchi is not None:
                login(request, foydalanuvchi)
                return redirect('readVazifa')  # Redirect to a success page after login
    else:
        formMe = AuthenticationForm()
    
    return render(request, 'accounts/loginFoydalanuvchi.html', {'formMe': formMe})


def logoutFoydalanuvchi(request):
    logout(request)
    return redirect('welcomeFoydalanuvchi')

#-------------------------------------------------------

@login_required
def profileFoydalanuvchi(request):
    return render(request, 'accounts/profileFoydalanuvchi.html')

@login_required
def changeProfile(request):
    context={
        "username_email": sozlangUserChangeForm(instance=request.user),
        
        "password": PasswordChangeForm(request.user),
    }
    return render(request, "accounts/changeProfile.html", context)

@login_required
def editFoydalanuvchi(request):
    if request.method == 'POST':
        formMe = sozlangUserChangeForm(request.POST, instance=request.user)
        if formMe.is_valid():
            formMe.save()
            update_session_auth_hash(request, request.user)
            return redirect('changeProfile')
    # else:
    #     formMe = sozlangUserChangeForm(instance=request.user)
    # return render(request, 'accounts/editFoydalanuvchi.html', {'formMe': formMe})


@login_required
def changeParolFoydalanuvchi(request):
    if request.method == 'POST':
        formMe = PasswordChangeForm(request.user, request.POST)
        if formMe.is_valid():
            formMe.save()
            return redirect('profileFoydalanuvchi')
    # else:
    #     formMe = PasswordChangeForm(request.user)
    # return render(request, 'accounts/changeParolFoydalanuvchi.html', {"formMe": formMe})


@login_required
def deleteFoydalanuvchi(request):
    request.user.delete()
    return redirect('welcomeFoydalanuvchi')