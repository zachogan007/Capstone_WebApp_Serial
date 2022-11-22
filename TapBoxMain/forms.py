'''from django import forms 

from .models import *

class UpdateResetValue(forms.ModelForm):

    reset_button = forms.CharField(max_length=5,required=True)

    class Meta: 
        model = Reset
        fields = ['reset_button']
'''