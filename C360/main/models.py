from django.db import models
from django.contrib.auth.models import User
from curriculum.models import department
from curriculum.models import department
from django.contrib.auth.models import AbstractUser
# Create your models here.

class myusers(AbstractUser):
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    department = models.ManyToManyField(department)

    def __str__(self):
        return self.username
