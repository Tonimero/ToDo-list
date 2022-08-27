from django.shortcuts import render
from .models import ToDo
from . forms import addTask
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.
# def index(request):
#     return HttpResponse('Home')

@login_required(login_url='login')
def index(request):
    # todos = ToDo.objects.all() #fetches all information from the table called todo in ascending order
    # todos = ToDo.objects.all()[:1] # returns only 1 value from the table called todo
    # todos = ToDo.objects.order_by('-created_at')[:1] # sorts the table and returns only 1 latestest value
    # todos = ToDo.objects.order_by('-created_at') # sorts the data and returns all the values in descending order
    user = User.objects.filter(username=request.user)
    todos = ToDo.objects.filter(author__in=user)
    form = addTask()
    context = {
        'todos':todos,
        'form': form
    }
    return render(request, 'folders/index.html', context)


def create_task(request):
    if request.method == 'POST':
        form = addTask(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'Task added successfully')
            return redirect('index')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('index')
    
    
def update_task(request, id):
    task = get_object_or_404(ToDo, id=id)
    if task.author != request.user:
        return redirect('index')
    else:
        form = addTask(instance=task)
        if request.method == 'POST':
            form = addTask(request.POST, instance=task)
            if form.is_valid():
                task = form.save()
                messages.success(request, 'Update successfully')
                return redirect('index')
            else:
                print("==",form.errors)
    context = {
    'form': form,
    'task': task
    }
    return render(request, 'folders/update.html', context)
    # if request.method == 'POST':
    #     task = get_object_or_404(ToDo, id=id)
    #     form = addTask(request.POST, instance=task)
    #     form.save()
    #     messages.success(request, 'Update successfully')
    #     return redirect('index')
    
    
    # if request.method == 'GET':
    #     form = addTask()
    #     context = {
    #         'form':form
    #     }

def delete_task(request, id):
    delete_todo = ToDo.objects.get(id = id)
    if delete_todo.author == request.user:
        delete_todo.delete()
        messages.success(request, 'deleted')
        return redirect('index')
    else:
        return redirect('index')
    # try:
    #     delete_todo = ToDo.objects.get(id = id)
    #     if delete_todo != request.user:
    #         return redirect('index')
    #     delete_todo.delete()
    # except ToDo.DoesNotExist:
    #     return redirect('index')
    # return redirect('index')

