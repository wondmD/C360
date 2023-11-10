from django.db import models
from curriculum.models import *
from main.models import *


class course(models.Model):
    name = models.CharField("Name", max_length=200)
    semister = models.ForeignKey(semister , on_delete=models.CASCADE, null=True)
    description =models.TextField()
    department = models.ManyToManyField(department) 
    prerequest = models.CharField(max_length=200, null=True, default='None')
    crh = models.IntegerField()
    st1 = 'Applied'
    st2 = 'Engineering'
    stream_choice = [
        (st1 , 'Applied'),
        (st2, 'Engineering')
    ]
    couree_type1 = "Mandatory"
    course_type2 = 'Elective'
    course_type3 = 'Free-Elective'
    course_typechoice = [
        (couree_type1, "Mandatory"),
        (course_type2, 'Elective'),
        (course_type3, 'Free-Elective')
    ]
    course_type = models.CharField(max_length=200, choices=course_typechoice,default=couree_type1)

    class Meta:
        ordering = ["-course_type", "name"]
    
    def __str__(self):
        return self.name

class CourseLike(models.Model):
    user = models.ForeignKey(myusers, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} likes {self.course.name}"

class resource(models.Model):
    name = models.CharField("Name", max_length=200)
    course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to="uploaded_resource")
    description = models.TextField()
    def __str__(self):
        return self.name



