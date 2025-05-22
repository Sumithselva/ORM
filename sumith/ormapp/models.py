from django.db import models
from django.contrib import admin
class Football(models.Model):
    playername = models.CharField(primary_key=True)
    age = models.IntegerField(max_length=50)
    nationality = models.CharField()
    club = models.CharField()
    position = models.CharField()
    
class Display(admin.ModelAdmin):
    list_display = ('playername','age','nationality','club','position')
