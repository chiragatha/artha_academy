from django.db import models

# Create your models here.
class Allcourses (models.Model):
    coursename = models.CharField(max_length=200)
    instructorname = models.CharField(max_length=200)
    def __str__(self):
        return self.coursename

class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    selfpaced = models.CharField(max_length=500)
    intructor_lead = models.CharField(max_length=500)
    def __str__(self):
        return self.selfpaced