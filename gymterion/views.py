from django.http import HttpResponse
from django.shortcuts import render
from .models import Record, Exercise


def index(request):
    records = Record.objects.all()
    exercises = Exercise.objects.all()
    context = {
            "exercises": exercises,
            "records": records,
            }
    return render(request, 'gymterion/index.html', context)
