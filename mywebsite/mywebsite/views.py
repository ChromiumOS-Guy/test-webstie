"""//myapp/views.py"""
from ast import Delete
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from urllib import request
from mywebsite.models import save_user_data
from email import message
#user
def home(request):
    if not request.user.is_authenticated:
        return redirect('/signin_promt')
    return render(request, 'home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/signin_promt')
    user_bio=save_user_data.objects.get(username = request.user.username)
    user=User.objects.get(id = request.user.id)
    context ={
        "user_bio":user_bio,
        "user":user
    }
    if request.method == 'POST':
        if request.POST.get('bio'):
            user_data=save_user_data.objects.get(username = request.user.username)
            user_data.bio=request.POST.get('bio')
            user_data.username=request.user.username
            user_data.save()
        if request.POST.get('email'):
            user=User.objects.get(id = request.user.id)
            user.email=request.POST.get('email')
            user.save()
        return redirect('/profile')
    else:
        return render(request, 'profile.html', context)

# Authentication
def change_user_password(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your password was successfully updated!',
                             extra_tags='alert-success')
            return redirect('/profile')
        else:
            return render(request, 'Authentication/changeuserpassword.html',{'form': form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'Authentication/changeuserpassword.html',{'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            createuserdata=save_user_data()
            createuserdata.username=username
            createuserdata.save()
            return redirect('/')
        else:
            return render(request, 'Authentication/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'Authentication/signup.html', {'form': form})
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'Authentication/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'Authentication/login.html', {'form': form})
  
def signin_promt(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'Authentication/signin.html')
   
def signout(request):
    logout(request)
    return redirect('/')

def delete_user(request):
    user=User.objects.get(id = request.user.id)
    user_data=save_user_data.objects.get(username = request.user.username)
    user.delete()
    user_data.delete()
    logout(request)
    return redirect('/')

# games
def snake_game(request):
    if not request.user.is_authenticated:
        return redirect('/signin_promt')
    return render(request, 'games/snake/index.html')

def pong_game(request):
    if not request.user.is_authenticated:
        return redirect('/signin_promt')
    return render(request, 'games/pong/index.html')

def the_2048_game(request):
    if not request.user.is_authenticated:
        return redirect('/signin_promt')
    return render(request, 'games/2048/index.html')

