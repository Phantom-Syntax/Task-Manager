from django.http import HttpResponse
from django.shortcuts import render
from manager_app.forms import SignForm,TaskForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def sign_user(request):
    if request.method=='POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Login page")
    else:
        form = SignForm()
    return render(request,'register.html',{'form':form})

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=name,password=pwd)
            if user is not None:
                login(request, user)
                return HttpResponse('Add task')
            else:
                messages.info(request,'Inccorect username or password')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def home(request):
    return render(request,'home.html')

def add_task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        pass





