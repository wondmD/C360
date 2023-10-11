from django.db import models





# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=100)

    SoANS='School of Applied Natural Sciences'
    SoCEA='School of Civil Engineering and Architecture'
    SoEEC='School of Electrical Engineering and Computing'
    SoMCME='School of Mechanical, Chemical, and Materials Engineering'
    none = 'none'

    school_options=[
        (SoANS,'School of Applied Natural Sciences'),
        (SoCEA,'School of Civil Engineering and Architecture'),
        (SoEEC,'School of Electrical Engineering and Computing'),
        (SoMCME,'School of Mechanical, Chemical, and Materials Engineering'),
        (none, 'none')
    ]
    school = models.CharField(
        max_length=100,
        choices=school_options,
        default=SoEEC
    )
    def __str__(self):
        return self.name
class level(models.Model):
    freshman = "freshman"
    school = "school"
    department= "department"

    leval_name_options= [
        (freshman, 'freshman'),
        (school, 'school'),
        (department, 'department')
    ]
    name = models.CharField(
        max_length=100,
        choices=leval_name_options,
        default=freshman
    )
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
    class Meta:
        ordering = ['year', 'semister_number']
        unique_together = ['year', 'semister_number']

    def __str__(self):
        return (self.year +' '+self.semister_number)




