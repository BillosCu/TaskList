from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def ListTask(request):#Get
    #Se puede consultar
    tareas = Task.objects.all()
    #print(tareas)
    context = {
        "Tareas": tareas[::-1], #Las lista en de más reciente a más viejo
        "update": None
    }
    return render(request,'task.html', context)


def createTask(request):
    task = Task(titulo=request.POST['titulo'], desc=request.POST['desc'])
    task.save() #POST
    return redirect('/')


def deleteTask(request, id):
    Tarea = Task.objects.get(id=id)
    Tarea.delete() #Delete
    return redirect('/')

def updateTask(request, id):
    Tareas = Task.objects.all()
    Tarea = Task.objects.get(pk=id)
    context = {
        "Tareas": Tareas[::-1], #Las lista en de más reciente a más viejo
        "update": Tarea
    }
    return render(request,'task.html', context)


def update(request):
    id = request.POST['id']
    NuevoTitulo = request.POST['titulo']
    NuevaDesc = request.POST['desc']
    task = Task.objects.get(pk=id)
    task.titulo = NuevoTitulo
    task.desc = NuevaDesc
    task.save()
    return redirect('/')