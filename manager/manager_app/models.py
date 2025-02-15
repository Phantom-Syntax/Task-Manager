from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30,null=False)
    content = models.TextField(max_length=100,null=False)
    date_posted = models.DateField(auto_now_add=True,null=False)
    user = models.ForeignKey(User,max_length=30,on_delete=models.CASCADE,null=False)