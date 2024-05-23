from .forms import TodoForms
from .models import TodoList
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def Todo(request):
    form = TodoForms
    todo = TodoList.objects.all()
    context = {
        'forms' : form,
        'todo' : todo
    }
    if request.method == 'POST':
        forms = TodoForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('todo')
    return render(request, 'index.html', context)


def DeleteTodo(request, id):
    todo_obj = TodoList.objects.get(id=id)
    if request.method == 'POST':
        todo_obj.delete()
        return redirect('todo')
    
    
def UpdateTodo(request, id): 
    todo_obj = TodoList.objects.get(id=id)
    form = TodoForms(instance=todo_obj)
    context = {
        'forms' : form
    } 
    if request.method == 'POST':
        form = TodoForms(request.POST, instance=todo_obj)
        if form.is_valid():
            form.save()
            return redirect("todo")
    return render(request, 'updatetodo.html', context)
