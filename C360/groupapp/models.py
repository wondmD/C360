from django.db import models
from main.models import myusers
from resource.models import course

# Create your models here.

class group(models.Model):
    host = models.ForeignKey(myusers, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        myusers, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
class Message(models.Model):
    user = models.ForeignKey(myusers, on_delete=models.CASCADE)
    room = models.ForeignKey(group, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to="groupapp/static/resource", blank=True, null=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

