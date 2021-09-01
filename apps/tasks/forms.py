from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('ower',)
        

class TaskForm(forms.ModelForm):

    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Task
        exclude = ('ower',)

        fields = (
            'name',  
            'descripition', 
            'end_date', 
            'priority',
            'category', 
            'status', 
        )

