from .models import Task
from django.forms import ModelForm,widgets,TextInput,Textarea


class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task",'nomer']
        widgets={'title': TextInput(attrs={'class ':'form-control','placeholder':'Введите название'}),
                 'nomer': TextInput(attrs={'class ':'form-control','placeholder':'Введите примечание'}),
                 'task': Textarea(attrs={'class ': 'form-control', 'placeholder': 'Текст'}),
                 }

