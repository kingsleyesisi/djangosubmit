from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

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
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Here you would typically validate the username and password
        # For now, we will just render the login page again
        
    
    return render(request, 'login.html')