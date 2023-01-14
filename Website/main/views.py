from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': ' Главная страница', 'tasks': tasks,'nomer':'nomer'})


def about(request):
    return render(request, 'main/about.html')


def set(request):
    return render(request, 'main/settings.html')

def create(request):
    error=''
    if request.method== 'POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error:'Форма была не верной'
    form= TaskForm()
    context={
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html',context)


def vxod(request):
    return render(request, 'main/vxod.html')
