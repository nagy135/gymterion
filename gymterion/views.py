from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Record, Exercise
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        return redirect('/gymterion/adder/')
    else:
        return redirect('/gymterion/log_in/')


def log_in(request):
    context = {
                "css": "log_in.css",
                "js": "log_in.js"
            }
    return render(request, 'gymterion/log_in.html', context)

def log_out(request):
    logout(request)
    return redirect('/gymterion/')

def adder(request):
    exercises = Exercise.objects.all()
    context = {
                "css": "adder.css",
                "js": "adder.js",
                "exercises": exercises
            }
    return render(request, 'gymterion/adder.html', context)

def add(request):
    user = User.objects.get(username=request.user)
    exercise = Exercise.objects.get(id=request.POST.get('exercise'))
    series = request.POST.get('series')
    weight = request.POST.get('weight')
    reps = request.POST.get('reps')
    note = request.POST.get('note')
    record = Record.objects.create(user=user, exercise=exercise, series=series, reps=reps, weight=weight, note=note)
    print(record.creation_date)
    record.save()
    return redirect('adder')

def statistics(request):
    exercises = Exercise.objects.all()
    context = {
                "css": "statistics.css",
                "js": "statistics.js",
                "exercises": exercises
            }
    return render(request, 'gymterion/statistics.html', context)

def do_authenticate(request):
    if request.user.is_authenticated:
        return redirect('/gymterion/')
    else:
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/gymterion/')
        else:
            return redirect('/gymterion/log_in/')
