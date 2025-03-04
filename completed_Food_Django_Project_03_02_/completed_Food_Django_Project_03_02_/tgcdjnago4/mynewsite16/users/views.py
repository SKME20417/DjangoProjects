from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username} , Your accound has been created successfully")
            return redirect("login")
    form = RegisterForm()
    return render(request, "users/register.html", {'form':form})


@login_required
def profilepage(request):
    return render(request, 'users/profile.html') 

def logoutview(request):
    logout(request)
    return render(request, 'users/logout.html')          