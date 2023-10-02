from django.db import models
from django.contrib.auth.models import User
from curriculum.models import department
from django.contrib.auth.models import AbstractUser
# Create your models here.

class myusers(AbstractUser):
    profile_pic = models.ImageField(upload_to="profilepic", height_field=None, width_field=None, max_length=None, default='profilepic/avatar.png')
    date_created = models.DateTimeField(auto_now_add=True , null=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
