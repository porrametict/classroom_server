from django.db import models

# Create your models here.

class TeachingPeriod(models.Model):
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Course(models.Model):
    course_id = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    teaching_period = models.ForeignKey(TeachingPeriod,on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=255)
    status = models.BooleanField()
