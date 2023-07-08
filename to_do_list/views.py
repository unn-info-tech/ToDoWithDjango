from django.http import HttpResponse

# CRUD

def create(request):
    return HttpResponse("Add a new one")

def read(request): #list of activities
    return HttpResponse("Your list of activities")

def update(request):
    return HttpResponse("Mark your activity")

def delete(request):
    return HttpResponse("Delete you activity")