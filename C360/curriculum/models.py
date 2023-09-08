from django.db import models
from resource.models import course



# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class semister(models.Model):
    year1 = '1st year'
    year2 = '2nd year'
    year3 = '3rd year'
    year4 = '4th year'
    year5 = '5th year'

    yearOptions= [
        (year1 , '1st year'),
        (year2 , '2nd year'),
        (year3 , '3rd year'),
        (year4 , '4th year'),
        (year5 , '5th year'),
    ]

    year = models.CharField(
        max_length=50,
        choices=yearOptions,
        default=year1)
    sem1 = "1st semister"
    sem2 = '2nd semister'

    semisterChoice = [
        (sem1 , "1st semister"),
        (sem2 , '2nd semister'),
    ]
    
    semister_number = models.CharField(
        max_length=50,
        choices=semisterChoice,
        default = sem1)
    courses = models.ManyToManyField(course)
    department_name = models.ForeignKey(department, on_delete=models.CASCADE)
    def __str__(self):
        return (self.year +' '+self.semister_number)



