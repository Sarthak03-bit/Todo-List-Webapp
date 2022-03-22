from importlib.resources import contents
from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from home.models import Task
# Create your views here.

def home(request):
    context= { 'success' :False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        ins=Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context= { 'success' :True}
    return render(request,'index.html', context)


def tasks(request):
    allTasks=Task.objects.all()
    cont= {'tasks': allTasks}
    return render(request,'tasks.html', cont)

def deleteTask(request, pk):
    queryset= Task.objects.get(id=pk)
    if request.method=="POST":
        queryset.delete()
        return redirect('/')
    context={
        'item':queryset
    }
    return render(request, 'delete_task.html', context)