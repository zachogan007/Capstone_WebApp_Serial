from django.db import models

# Create your models here.


#models represent database tables-- variable information that we need to know
#each model field represents a database table field entry. 
#BE SURE to run py manage.py makemigrations TapBoxPages if changes to models are made
#Once all changes are ready, run py manage.py migrate
#The DB schema will have to be updated.
#Migrations are powerful and allow us to make changes TO MODELS over time. 
class BatteryMonitorStatus(models.Model): #Battery monitor object for DB
    battery_text = models.CharField(max_length = 1000)
    batter_status = models.ImageField
    curr_date_time = models.DateTimeField('Status time')
    def __str__(self):
        return self.battery_text
#can play around with model fields by using the command py manage.py shell
#1) > from TapBoxPages.mdoels import BatteryMonitorStatus
#2) from django.utils import timezone
#3) battery = BatteryMonitorStatus(battery_text = "The current battery status:", curr_date_time = timezone.now())
class Reset(models.Model): #Reset object for DB
    reset_intstruction = models.CharField(max_length = 100)
    reset_button = models.BooleanField
    def __str__(self):
        return self.reset_intstruction

class logRecord(models.Model): #logRecord object for DB
    last_unlock_text = models.CharField(max_length = 100)
    last_unlock_time = models.DateTimeField('Last unlock time')



