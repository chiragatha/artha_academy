from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=200)
    instructor_name=models.CharField(max_length=200)
    def __str__(self):
        return self.course_name


class Details(models.Model):
    courses=models.ForeignKey(Courses, on_delete=models.CASCADE)
    self_paced=models.CharField(max_length=500)
    intructor_lead=models.CharField(max_length=500)
    def __str__(self):
        return str(self.pk)

class Lectures(models.Model):
    video = models.ForeignKey(Courses, on_delete=models.CASCADE)
    file_type = models.CharField(max_length= 10)
    lecture = models.FileField(upload_to='lectures',default='')
    video_title = models.CharField(max_length=200)
    def __str__(self):
        return self.video_title

class Notes(models.Model):
    notes = models.ForeignKey(Courses,on_delete=models.CASCADE)
    notes_title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs')
    def __str__(self):
        return self.notes_title

