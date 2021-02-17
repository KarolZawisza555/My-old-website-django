from django import forms
from .models import Report, Holiday_request, Task
from django.contrib.admin import widgets 
from django.forms.widgets import NumberInput
from django.utils import timezone

TODAY = timezone.now().date()
BEGIN = timezone.datetime(2021,1,1).date()

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('team','product_A','product_B','description')


class DayForm(forms.Form):
    day_1 = forms.DateField(label='Begin',initial = BEGIN,widget=NumberInput(attrs={'type': 'date'}))
    day_2 = forms.DateField(label='End',initial = TODAY,widget=NumberInput(attrs={'type': 'date'}))


class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday_request
        fields = ('first_name','surname','email','department','date_begin','date_end','notice')
        widgets = { 'date_begin': NumberInput( attrs={'type': 'date'}),
                    'date_end': NumberInput(attrs={'type': 'date'}),
                     }

class TaskForm(forms.Form):
    title =forms.CharField(max_length=150,label="Creata a new task")

    
    
