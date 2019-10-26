from django.db import models
from datetime import datetime 
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class SkillSet(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    languages = models.CharField(max_length=100,default='')
    frameworks = models.CharField(max_length = 100 ,default='')
    gpa = models.FloatField()
    company = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.user.username
