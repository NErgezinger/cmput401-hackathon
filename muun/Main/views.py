from Main.models import Calendar
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *


def home(request):
    return HttpResponse('homepage')


def profile(request):
    return render(request, 'Main/profile.html', context={'user': request.user})




def day_mood(request):
    user = request.user

    if request.method == 'GET':
        return render(request, 'Main/day_mood.html')

    elif request.method == 'POST':
        pass


def test_data(request):
    Calendar.objects.all().delete()
    Calendar.objects.create(data = {
            'name' : 'john cena',
            'activities' : ['stacking bread'],
            'score' : '5'
        })

    Calendar.objects.create(data = {
            'name' : 'kishan cena',
            'activities' : ['studying'],   
            'score' : '1'
        })

    Calendar.objects.create(data = {
            'name' : 'ayman cena',
            'activities' : ['napping'],
            'score' : '14'
        })

    Calendar.objects.create(data = {
            'name' : 'John cena Jr',
            'activities' : ['Wrestling', 'Boxing'],
            'score' : '5'
        })

    print(Calendar.data)

# def create_account(request):
#     if request.method == 'GET':
#         return HttpResponse('create account')
#     elif request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create(form['username'], '', form['password'])
#             user.save()
#             login(request, user)
#             return redirect(profile)


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'Main/login.html')

#     elif request.method == 'POST':
#         data = request.POST
#         user = authenticate(username=data['username'], password=data['password'])
#         if user is not None:
#             login(request, user)
#             return redirect(profile)
#         else:
#             return redirect(profile)


# def logout(request):
#     logout(request)
#     return HttpResponseRedirect('/')