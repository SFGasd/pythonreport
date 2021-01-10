from django.db import models
from django.utils import timezone

# Create your models here.

class AccessInfo(models.Model):
    access_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-access_time',)

    def __str__(self):
        return self.access_time
    
class PlayList(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    wiki = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class TaipeiStationInOut(models.Model):
    name = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    io_class = models.CharField(max_length=20)
    io_amount = models.CharField(max_length=20)

    def __str__(self):
    	return self.name

class TaipeiStationExtraData(models.Model):
    year_date = models.CharField(max_length=10)
    total_mileage = models.CharField(max_length=10)
    total_persontimes = models.CharField(max_length=20)
    total_income = models.CharField(max_length=20)

    def __str__(self):
    	return self.year_date
