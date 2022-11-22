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

##GOALS FOR MONDAY: CREATE FORMS FOR THE RESET TO STORE WHEN RESET IS TRUE___DONE
##ALSO, MAKE SURE TO RESEARCH NETWORKING SERIAL INTERFACE FOR RESET__ 
##IF TIME ALLOTS, TEST ON MSP 


def loginpage(request):
    return HttpResponse("Ya better login to this gosh dern tapbox boi. On my tractor. Praise the LAWD")


def mainpage(request):
    template = loader.get_template('TapBoxMain/tapboxmain.html')
    battery = BatteryMonitorStatus.objects.all()
    reset = Reset.objects.all()
    deleteOldVals = Reset.objects.all() 
    deleteOldVals.delete() #might need to change to "edit model" instead based on id number
    time = logRecord.objects.order_by('-last_unlock_time')[:]
    context = {
        'time': time,
        'reset' : reset,
        'battery' : battery,
    }



    Reset.reset_button = "False"
    print(Reset.reset_button)
    if request.method == 'POST':
        if 'TRUE' == request.POST.get('reset'):

            resetVal = request.POST.get('reset', "FALSE")

            print(Reset.reset_button)
            

            ##### FILLL OUT SERIAL IMPLEMENTATION #####
            newResetVal = Reset.objects.create(reset_button = resetVal)
            newResetVal.save()
            #newResetVal = Reset.objects.create(reset_button = "FALSE")
            #newResetVal.save() ##NEED TO SET DEFAULT RESET TO FALSE-- IMPLEMENT

    


    return HttpResponse(template.render(context,request))

def logoutPage(request):
    template = loader.get_template('TapBoxMain/logout.html')
    return render(request, 'TapBoxMain/logout.html')


