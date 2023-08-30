from django.db import models

class resource(models.Model):
    name = models.CharField("Name", max_length=250)
    file = models.FileField(upload_to="resource/static/resource")
    description = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField("Name", max_length=200)
    description =models.TextField()
    resource= models.ManyToManyField(resource)
    crh = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.name


