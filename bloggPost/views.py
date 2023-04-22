from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.

# signin page


def signinPage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pass1 = request.POST.get('pass')
        print(name, pass1)

        user = authenticate(username=name, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'signin.html')

# signup page


def signupPage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = User.objects.create_user(
            username=name, password=password,  email=email
        )
        user.save()

    return render(request, "signup.html")

# home Page


def homePage(request):
    post = blogg.objects.all()

    return render(request, 'home.html', {'post': post})

# logou Page


def logoutPage(request):
    logout(request)
    return redirect('/')

# add post


def AddPost(request):
    if request.method == "POST":
        tital = request.POST.get('Post_tital')
        content = request.POST.get('Post_content')
        post = blogg(bloggtitle=tital, bloggContent=content)
        post.save()
        return redirect('home')

    return render(request, 'Addpost.html')
