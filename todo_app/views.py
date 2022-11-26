from django.shortcuts import render,redirect
import datetime
from .models import *
from todo_app.models import *
from django.contrib import messages
from datetime import date

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

#code Here 
def add_todo(request):
    if request.method == "POST":
        title = request.POST['title'] or None
        content = request.POST['content']
        created_at = datetime.datetime.now()
        if content != None:
            todo_obj = Todo_Task(title=title,content=content,created_at=created_at)
            todo_obj.save()
            message = 'Todo added successfully.'
            messages.success(request, message)
            return redirect("/todo_lists")
        else:
            message = 'Please enter a filed. '
            messages.success(request, message)

    
    return render(request,'add_todo.html')



def view_todo_details(request):
    try:
        todo_obj = Todo_Task.objects.all()
        context={'todo_obj':todo_obj}
    except:
        messages.warning(request, "sorry try again")
    return render(request,'todo_lists.html',context)






def delete(request,pk):
    todo_obj= Todo_Task.objects.filter(id=pk)
    print("todo_obj",todo_obj)

    context = {'todo_obj': todo_obj}
    if request.method == "POST":
        customer_del_obj= Todo_Task.objects.filter(id=pk).delete()
        todo_obj = Todo_Task.objects.all()
        print(todo_obj)
        context={'todo_obj':todo_obj}
        message = 'TODO Task Delete successfully.'
        messages.success(request, message)
        print("-----context-",context)
        return render(request,'todo_lists.html',context)


    return render(request,'delete_todo.html',context)


def mark_completed(request, pk): 
    todo_obj= Todo_Task.objects.filter(id=pk)
    print("user_obj",todo_obj)

    context = {'todo_obj': todo_obj}
    if request.method == "POST":
        customer_del_obj= Todo_Task.objects.filter(id=pk).update(task_status=True)
        user_obj = Todo_Task.objects.all()
        print(todo_obj)
        context={'user_obj':todo_obj}
        message = 'TODO Marked Completed successfully.'
        messages.success(request, message)
        print("-----context-",context)
        return redirect("/todo_lists")


    return render(request,'mark_completed.html',context)



def completed_task(request):
    try:
        todo_obj = Todo_Task.objects.filter(task_status=True)
        context={'todo_obj':todo_obj}
    except:
        messages.warning(request, "sorry try again")
    return render(request,'completed_task.html',context)

def pending_task(request):
    try:
        todo_obj = Todo_Task.objects.filter(task_status=False)
        context={'todo_obj':todo_obj}
    except:
        messages.warning(request, "sorry try again")
    return render(request,'pending_task.html',context)





