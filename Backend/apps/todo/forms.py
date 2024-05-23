from django import forms
from .models import TodoList
from django.forms import TextInput


class TodoForms(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title']
        widgets = {
            'title': TextInput(attrs = {
            'type': "text", 
            'class': "form-control",
            'placeholder': "Enter ur todo"
            })
        }
