from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    creation_date = models.DateTimeField('creation_date', auto_now_add=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    series = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    note = models.CharField(max_length=200)

    def __str__(self):
        return str(self.weight)
