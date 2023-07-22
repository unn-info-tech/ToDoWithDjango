from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import sozlangUserCreationForm


# Create your views here.



# User Sign Up, Sign In

def registerFoydalanuvchi(request):
    if request.method == "POST":
        formMe = sozlangUserCreationForm(request.POST)
        if formMe.is_valid():
            # foydalanuvchi = formMe.save(commit=False)
            # foydalanuvchi.is_staff = True
            formMe.save()
            redirect("loginFoydalanuvchi")
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