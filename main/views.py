from django.shortcuts import render, redirect
from .models import Tutorial
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'tutorials': Tutorial.objects.all()})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account Created for {username}')
            login(request, user)
            messages.info(request, f'You are now logged in as {username}')
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')

    form = NewUserForm
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)


def logout_account(request):
    logout(request)
    messages.info(request, f'Logged out succesfully')
    return redirect("main:homepage")


def login_account(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect("main:homepage")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'main/login.html', context)

