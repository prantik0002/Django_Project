from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    question= models.CharField(max_length=1000)
    option_a=models.IntegerField()
    option_b=models.IntegerField()
    option_c=models.IntegerField()
    option_d=models.IntegerField()
    answer=models.IntegerField()

class exam_user(models.Model):
        user=models.OneToOneField(User, on_delete=models.CASCADE)
        real_name=models.CharField(max_length=40)
