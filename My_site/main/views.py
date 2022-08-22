from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm

def index(request):
    tasks=Task.objects.order_by('-id')
    return render(request,'main/index.html',{'title':'Главная страница сайта','tasks':tasks})

def contacts(request):
    return HttpResponse("<h1>Contacts</h1>")

def about(request):
    return render(request,'main/about.html')

def YDC(request):
    return HttpResponse("<h1>Курс молодого разработчика</h1>")

def create(request):
    error=''
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма заполнена неверно'
    form=TaskForm()
    context={
        'form':form,
        'error':error
    }
    return render(request,'main/create1.html',context)


