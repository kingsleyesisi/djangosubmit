from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    """
    Render the index page of the stock management application.
    """
    return render(request, 'index.html')


def login(request):
    
    """
    render login page and validate input 
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Here you would typically validate the username and password
        # For now, we will just render the login page again
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, redirect to index or another page
            return render(request, 'index.html')
        else:
            print("Invalid credentials")
            # Invalid credentials, render login page with error
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')


def register(request):
    """
    This is to register a new user.
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # here to crate the user 
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password
                                        )
        user.save() # to save the user to the database
         
    return render(request, 'register.html')

