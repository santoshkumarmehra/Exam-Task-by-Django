from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200, null=True)
    option_1 = models.CharField(max_length=200, null=True)
    option_2 = models.CharField(max_length=200, null=True)
    option_3 = models.CharField(max_length=200, null=True)
    option_4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)

class Result(models.Model):
    student_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,null=True)
    result = models.CharField(max_length=200, null=True)


class UserData(models.Model):
    user = models.CharField(max_length=200, null=True)
    result = models.CharField(max_length=200, null=True)
