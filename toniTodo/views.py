from django.shortcuts import render
from .models import ToDo
from . forms import addTask
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

# Create your views here.
# def index(request):
#     return HttpResponse('Home')
def index(request):
    # todos = ToDo.objects.all() #fetches all information from the table called todo in ascending order
    # todos = ToDo.objects.all()[:1] # returns only 1 value from the table called todo
    # todos = ToDo.objects.order_by('-created_at')[:1] # sorts the table and returns only 1 latestest value
    todos = ToDo.objects.order_by('-created_at') # sorts the data and returns all the values in descending order
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
            form.save()
            messages.success(request, 'Task added successfully')
            return redirect('index')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('index')
    
    
def update_task(request, id):
    task =get_object_or_404(ToDo, id=id)
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
        
    

