from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class LeaveData(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    leave_from = models.DateField()
    leave_bal = models.IntegerField(default=20)
    leave_days = models.IntegerField()
    leave_status = models.CharField(max_length=50)


    def __str__(self):
        return self.email
