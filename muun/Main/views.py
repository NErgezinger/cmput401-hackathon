from Main.models import Calendar
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from collections import Counter
import math

from .models import *

def home(request):
    return redirect(day_mood)


def index(request):
    return render(request, 'Main/index.html')


def day_mood(request):
    if request.method == 'GET':
        return render(request, 'Main/day_mood.html')

    elif request.method == 'POST':
        if Calendar.objects.count() == 0:
            Calendar.objects.create(data={})

        calendar = Calendar.objects.all()[0]

        time_ymd = datetime.now().strftime(r'%Y/%m/%d')

        calendar.data[time_ymd] = {}
        calendar.data[time_ymd]['mood'] = int(request.POST['mood'])

        calendar.save()

        return redirect(activities)


def activities(request):
    if Calendar.objects.count() == 0:
        Calendar.objects.create(data={})

    calendar_obj = Calendar.objects.all()[0]
    calendar = calendar_obj.data

    time_ymd = datetime.now().strftime(r'%Y/%m/%d')

    if time_ymd in calendar and 'activities' in calendar[time_ymd]:
        activities_list = calendar[time_ymd]['activities']
    else:
        activities_list = []

    if request.method == 'GET':
        return render(request, 'Main/activities_form.html', context={'activities': activities_list})

    elif request.method == 'POST':
        if request.POST['type'] == 'add':
            if time_ymd not in calendar:
                calendar[time_ymd] = {}
            if 'activities' not in calendar[time_ymd]:
                calendar[time_ymd]['activities'] = []

            calendar[time_ymd]['activities'].append(request.POST['activity'])
            calendar_obj.save()
            return redirect(activities)

        elif request.POST['type'] == 'delete':
            if time_ymd in calendar and 'activities' in calendar[time_ymd] and request.POST['activity'] in calendar[time_ymd]['activities']:
                calendar[time_ymd]['activities'].remove(request.POST['activity'])
            calendar_obj.save()
            return redirect(activities)


def summary(request):
    calendar = Calendar.objects.all()[0].data
    print(calendar)

    moods = ['amazing', 'good', 'neutral', 'bad', 'terrible']

    days = []
    mood_list = []

    for day, data in calendar.items():
        if 'mood' in data:
            days.append(day)
            mood_list.append(data['mood'])

    mood_counts = Counter(mood_list)

    mood_counts_ordered = [mood_counts[2], mood_counts[1], mood_counts[0], mood_counts[-1], mood_counts[-2]]

    return render(request, 'Main/summary.html', context={'mood_list': moods, 'mood_counts': mood_counts_ordered})


def test_data(request):
    Calendar.objects.all().delete()

    c = Calendar.objects.create(data = {
        '2021/09/11': {
            'activities' : ['activity1', 'activity2', 'activity3'],
            'mood' : 1
        },
        '2021/09/10': {
            'activities': ['activity2', 'activity4'],
            'mood': 2
        }
        })
    c.save()
    activities = []
    for x in (Calendar.objects.all()[0].data.values()):
        for activity in x['activities']:
            activities.append(activity)
    activities = set(activities)
    print(activities)
    activityScores = {}
    for activity in activities:
        total = 0
        count = 0
        print('test')
        for x in (Calendar.objects.all()[0].data.values()):
            if activity in x['activities']:
                total += int(x['mood'])
                count += 1
        activityScores[activity] = total/count
    print(activityScores)
        
    activityScores = dict(sorted(activityScores.items(), key = lambda item : item[1]))
    sortedScores = list(activityScores.items())
    print(sortedScores)

    # length = len(activityScores)
    # fifth = length/5
    # for x in range(5):
    #     print(str(x+1) + ' ' + sortedScores[round(fifth)][0])
    #     fifth += length/5
    
    

    return HttpResponse('test')

    
        

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