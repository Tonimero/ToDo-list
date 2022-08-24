from django.shortcuts import render
from .models import ToDo
from . forms import addTask
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

# Create your views here.
# def index(request):
#     return HttpResponse('Home')
def index(request):
    # todos = ToDo.objects.all() #fetches all information from the table called todo in ascending order
    # todos = ToDo.objects.all()[:1] # returns only 1 value from the table called todo
    # todos = ToDo.objects.order_by('-created_at')[:1] # sorts the table and returns only 1 latestest value
    todos = ToDo.objects.order_by('-created_at') # sorts the data and returns all the values in descending order
    desc = ToDo.objects.order_by('created_at')
    form = addTask()
    context = {
        'todos':todos,
        'form': form
    }
    return render(request, 'folders/index.html', context)

# when thr form is submitted
def create_task(request):
    if request.method == 'POST':
        form = addTask(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully')
            return redirect('index')
        else:
            messages.warning(request, 'Error: Task or Description field is empty')
            return redirect('index')
    
    
