from django.shortcuts import render, redirect, HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def singe_slug(request, single_url):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_url in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_url)

        series_obj = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest('tutorial_publish')
            series_obj[m] = part_one

        context = {
            'part_one': series_obj
        }
        return render(request, 'main/category.html', context)

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_url in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_url)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_publish')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        context = {
            'tutorial': this_tutorial,
            'sidebar': tutorials_from_series,
            'this_tut_idx': this_tutorial_idx
        }
        return render(request, 'main/tutorial.html', context)


def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={'categories': TutorialCategory.objects.all()})


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
