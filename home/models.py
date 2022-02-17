from django.db import models
from django.utils import timezone

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default=None, blank=True, null=True)
    mail = models.CharField(max_length=200,default=None, blank=True, null=True)

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    half = models.BooleanField(default=0)
    date = models.DateField(default=timezone.now)
    place = models.CharField(max_length=200,default=None, blank=True, null=True)
    work = models.CharField(max_length=200,default=None, blank=True, null=True)
    mentor = models.ForeignKey(Participant,on_delete=models.CASCADE,related_name='mentor',default=None, blank=True, null=True)
    mentee = models.ForeignKey(Participant,on_delete=models.CASCADE,related_name='mentee',default=None, blank=True, null=True)




