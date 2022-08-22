from django.forms import ModelForm,widgets,TextInput,Textarea,NumberInput
from . models import Task
from dataclasses import fields

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task","grade"]
        widgets={
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "grade": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите максим. балл'
            }),
        }