from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.forms import LoginForm, SignUpForm
from user_profile.models import Profile


def signin(request):
    if request.method == 'GET':
        if 'Logout' in request.GET:
            logout(request)
        loginForm = LoginForm()
        return render(request, 'user/login.html', {'form': loginForm, 'title_site': 'Log in'})
    elif request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            user = authenticate(User, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home', page=1)
        return render(request, 'user/login.html', {'form': loginForm, 'title_site': 'Log in'})


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form': form, 'title_site': 'Sign up'})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = Profile(user=user)
            profile.save()
            return redirect('login')
        return render(request, 'user/signup.html', {'form': form, 'title_site': 'Sign up'})
