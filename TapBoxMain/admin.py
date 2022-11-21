from django.contrib import admin
from django.contrib.sites.models import Site
from .models import *


admin.site.register(BatteryMonitorStatus)
admin.site.register(User)
admin.site.register(Reset)
admin.site.register(logRecord)
# Register your models here.
