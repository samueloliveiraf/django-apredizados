from django import forms
from .models import *


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('ower',)
        

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('ower',)

