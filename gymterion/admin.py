from django.contrib import admin

# Register your models here.

from .models import Record, Exercise

admin.site.register(Record)
admin.site.register(Exercise)
