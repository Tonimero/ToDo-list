from django import forms
from . models import ToDo

class addTask(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']