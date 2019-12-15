from django.shortcuts import render,redirect
from django.http import HttpResponse
from TaskPerformer.models import TaskList
from TaskPerformer.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    context={
        'welcome_text':"welcome to home page"
    }
    return render(request,'index.html',context)


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task has been added..."))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks,3)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request,'todolist.html',{'all_tasks':all_tasks})


def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    messages.success(request,("Task deleted..."))
    return redirect('todolist')



def edit_task(request,task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None ,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited..."))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request,'edit_task.html',{ 'task_obj': task_obj })
    


def completed(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('todolist')


def pending(request,task_id):
    task = TaskList.objects.get(pk=task_id) 
    task.done=False
    task.save()
    return redirect('todolist')



def contact(request):
    context={
        'welcome_text':"welcome to contact us"
    }
    return render(request,'contact.html',context)


def about(request):
    context={
        'welcome_text':"welcome to about us"
    }
    return render(request,'about.html',context)