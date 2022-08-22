from django.shortcuts import render
from .models import ToDo

# Create your views here.

# Create your views here.
# def index(request):
#     return HttpResponse('Home')
def index(request):
    # todos = ToDo.objects.all() #fetches all information from the table called todo in ascending order
    # todos = ToDo.objects.all()[:1] # returns only 1 value from the table called todo
    # todos = ToDo.objects.order_by('-created_at')[:1] # sorts the table and returns only 1 latestest value
    todos = ToDo.objects.order_by('-created_at') # sorts the data and returns all the values in descending order
    context = {
        'todos':todos,
    }
    return render(request, 'folders/index.html', context)