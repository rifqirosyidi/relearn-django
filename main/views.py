from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'tutorials': Tutorial.objects.all()})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)

