from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'authenticate/index.html')

def login_user(request):
    if request.method == "POST": #if the form is submitted
        username = request.POST['username'] # grab the username
        password = request.POST['password'] # grab the password
        user = authenticate(request, username=username, password=password)
        if user is not None: # if the user matches the database entry, log them in
            login(request, user)
            # Redirect to a success page.
            return redirect ('home')
        else: 
            # Returns error message.
            messages.success(request, ("There Was An Error Logging In. Try Again..."))
            # Return to login page
            return redirect ('login')
    else:
        return render(request, 'authenticate/login.html')