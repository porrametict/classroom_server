from django.db import models
import uuid


def random_course_code():
    return uuid.uuid4().hex[:8].upper()


# Create your models here.

class TeachingPeriod(models.Model):
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Course(models.Model):
    course_id = models.SlugField(unique=True, default=random_course_code)
    name = models.CharField(max_length=255)
    teaching_period = models.ForeignKey(TeachingPeriod, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=255)
    status = models.BooleanField()
