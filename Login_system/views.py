from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'authenticate/index.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if not User.objects.filter(username=username, email=email).exists():
            if password == confirm_password:
                user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Registered Successfully')
                return redirect('index')
            else:
                return HttpResponse('Password mismatch')
        else:
            return HttpResponse('Username or email already taken')
    else:
        return render(request, 'authenticate/register.html')

def login_user(request):
    if request.method == "POST": #if the form is submitted
        username = request.POST['username'] # grab the username
        password = request.POST['password'] # grab the password
        user = authenticate(request, username=username, password=password)
        if user is not None: # if the user matches the database entry, log them in
            login(request, user)
            # Redirect to a success page.
            return redirect ('index')
        else: 
            # Returns error message.
            messages.success(request, ("There Was An Error Logging In. Try Again..."))
            # Return to login page
            return redirect ('login')
    else:
        return render(request, 'authenticate/login.html')
    

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')