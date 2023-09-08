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
    couree_type1 = "Mandatory"
    course_type2 = 'Elective'
    course_type3 = 'Free-Elective'
    course_typechoice = [
        (couree_type1, "Mandatory"),
        (course_type2, 'Elective'),
        (course_type3, 'Free-Elective')
    ]
    course_type = models.CharField(max_length=200, choices=course_typechoice,default=couree_type1)
    def __str__(self):
        return self.name


