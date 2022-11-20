from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

from .models import BatteryMonitorStatus


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

#from .filters import ReviewFilter
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.views import generic
#from .models import Listing
from django.utils import timezone
#from .filters import OrderFilter

from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe

from .models import *
#from .calendar import Calendar
import calendar
#from .forms import UpdateUserForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginpage(request):
    return HttpResponse("Ya better login to this gosh dern tapbox boi. On my tractor. Praise the LAWD")


def mainpage(request):
    template = loader.get_template('TapBoxMain/tapboxmain.html')
    return render(request, 'TapBoxMain/tapboxmain.html')

def logoutPage(request):
    
  return HttpResponse("GET YO ARSE BACK HEEYAH BOI! ON GOURD! PRAISE THE LAWD!")

