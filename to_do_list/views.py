# from django.shortcuts import render, redirect
# from .models import Todo
# from .forms import TodoForm
from django.http import HttpResponse

# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, 'todo/todo_list.html', {'todos': todos})

# def todo_create(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForm()
#     return render(request, 'todo/todo_form.html', {'form': form})

# def todo_update(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'todo/todo_form.html', {'form': form})

# def todo_delete(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.delete()
#     return redirect('todo_list')

def check(request):
    return HttpResponse("Hello world")