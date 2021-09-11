from Main.models import Calendar
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

from .models import *

def home(request):
    return HttpResponse('homepage')


def profile(request):
    return render(request, 'Main/profile.html', context={'user': request.user})




def day_mood(request):
    user = request.user

    if request.method == 'GET':
        return render(request, 'Main/day_mood.html')

    elif request.method == 'POST':
        if Calendar.objects.count() == 0:
            Calendar.objects.create(data={})

        calendar = Calendar.objects.all()[0]

        time_ymd = datetime.now().strftime(r'%Y/%m/%d')

        calendar.data[time_ymd] = {}
        calendar.data[time_ymd]['mood'] = request.POST['mood']

        calendar.save()

        return redirect(profile)

def test_data(request):
    Calendar.objects.all().delete()

    c = Calendar.objects.create(data = {
        '2021/09/11': {
            'activities' : ['stacking bread'],
            'score' : '5'
        },
        '2021/09/10': {
            'activities' : ['activity 2'],
            'score' : '2'
        }
        })


    c.data['2021/09/11']['activities'] = ['changed']


    c.data["new date"] =  {
            'activities' : ['activity 3'],
            'score' : '3'
        }

    c.save()

    total = 0
    count = 0
    for x in (Calendar.objects.all()[0].data.values()):
        total += int(x['score'])
        count += 1 
    
    print(total/count)

        

    # score = 0
    # for x in c.values():
    #     score += c.values[1]


    #c.save()

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