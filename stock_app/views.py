from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

# Index view: renders the home page of the stock management app
def index(request):
    """
    Render the index page of the stock management application.
    """
    return render(request, 'index.html')

# Login view: handles GET (show login form) and POST (validate credentials)
def login(request):
    """
    Render login page and validate input 
    """
    if request.method == 'POST':
        # Get username and password from submitted form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication successful, log user in and redirect to dashboard
            auth_login(request, user)  # Log the user in
            print('login successful')
            return redirect('dashboard')
        else:
            # If authentication fails, show error message
            print("Invalid credentials")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    # If GET request, render login form
    return render(request, 'login.html')

# Register view: handles user registration
def register(request):
    """
    This is to register a new user.
    """
    if request.method == 'POST':
        # Get registration details from form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create new user
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password
                                        )
        user.save()
         
    # Render registration form
    return render(request, 'register.html')

# Dashboard view: only accessible to logged-in users
@login_required(login_url='login')
def dashboard(request):
    """
    The dashboard page for logged-in users.
    """
    # Render dashboard and pass user info to template
    return render(request, 'dashboard.html', {'user': request.user})