from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

from .models import BatteryMonitorStatus

# Create your views here.

def loginpage(request):
    template = loader.get_template('TapBoxMain/login.html')
    return render(request, 'TapBoxMain/login.html')
    return HttpResponse("Ya better login to this gosh dern tapbox boi. On my tractor. Praise the LAWD")


def mainpage(request):
    template = loader.get_template('TapBoxMain/tapboxmain.html')
    return render(request, 'TapBoxMain/tapboxmain.html')

def logoutPage(request):
    
  return HttpResponse("GET YO ARSE BACK HEEYAH BOI! ON GOURD! PRAISE THE LAWD!")

