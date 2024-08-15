from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    todos = Todo.objects.all()  # Fetch all tasks
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Todo.objects.create(title=title)
    return redirect('todoapp:todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        todo.delete()
    return redirect('todoapp:todo_list')

def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        todo.completed = True  # Mark task as completed
        todo.save()
    return redirect('todoapp:todo_list')

