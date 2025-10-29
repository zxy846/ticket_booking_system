from django.shortcuts import render
from django.http import HttpResponse

def passenger_register(request):
    return render(request, 'passengers/register.html')

def passenger_login(request):
    return render(request, 'passengers/login.html')

def passenger_logout(request):
    return HttpResponse("登出功能待实现")

def passenger_profile(request):
    return render(request, 'passengers/profile.html')

def passenger_profile_edit(request):
    return render(request, 'passengers/profile_edit.html')