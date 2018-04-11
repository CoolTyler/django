from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.

#  "/"
def index(request):
  return render(request, 'login_app/index.html')

# "/register"
def register(request):
  results = User.objects.validate(request.POST)
  if results['status'] == True:
    user = User.objects.creator(request.POST)
    messages.success(request, "User has been registered")
  else:
    for error in results['errors']:
      messages.error(request, error)
  return redirect('/')

# "/login"
def login(request):
  results = User.objects.validate_login(request.POST)
  if results['status'] == False:
    messages.error(request, "Email and password do not match")
    return redirect('/')
  request.session['email'] = results['user'].email
  request.session['first_name'] = results['user'].first_name
  return redirect('/dashboard')

# "/dashboard"
def dashboard(request):
  if 'email' not in request.session:
    return redirect('/')
  return render(request, "login_app/dashboard.html")

# "/logout"
def logout(request):
  request.session.flush()
  return redirect('/')