from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import UserRegisterForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record
from django.http import Http404
from django.contrib import messages
def index(request):  
    return  render(request, 'crud/index.html',)

# - register a user

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, 'registration was succesfull! ')
            
            return redirect('my-login')
        
    else:
            form = UserRegisterForm()
        
    context = {'form':form}
    return render(request, 'crud/register.html', context=context)

def my_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
            form = LoginForm()
        
    context = {'form':form}
    
    return render(request, 'crud/my-login.html', context=context)


@login_required(login_url='my-login')
def dashboard(request):
    user_record = Record.objects.filter(user=request.user)
    context = {'user_record':user_record}
    return render(request, 'crud/dashboard.html', context=context)

def create_record(request):
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            user_record = form.save(commit=False)
            user_record.user = request.user
            user_record.save()
            
            messages.success(request, 'record created sucessfully! ')
            return redirect('dashboard')
    
    else:
        form = CreateRecordForm()
        
    context = {"form":form}
    return render(request, 'crud/create-record.html', context=context)


@login_required(login_url='my-login')
def my_logout(request):
   logout(request)
   
   messages.success(request, 'logged out!')
   return redirect('my-login')

@login_required(login_url='my-login')
def view_record(request, pk):
    record = get_object_or_404(Record, user=request.user, id=pk)
    context = {'record':record}
    return render(request, 'crud/view-record.html', context=context)

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = get_object_or_404(Record, user=request.user, id=pk)
    record.delete()
    return redirect('dashboard')

@login_required(login_url='my-login')
def update_record(request, pk):
    user_record = get_object_or_404(Record, user=request.user, id=pk)
    
    if request.method == 'POST':
    
        form = UpdateRecordForm(request.POST, instance=user_record)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'update successful! ')
            return redirect('dashboard')
        
    else:
        form = UpdateRecordForm(instance=user_record)
        
    context = {'form':form, 'user_record':user_record}
    
    return render(request, 'crud/update-record.html', context=context)
    
    


            
    
    