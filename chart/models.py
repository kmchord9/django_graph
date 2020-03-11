from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class TempData(models.Model):
    date = models.DateTimeField(default=timezone.now)
    temp = models.FloatField()

admin.site.register(TempData)