from django.db import models
from course import models as course_models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=255)
    course_id = models.ForeignKey(course_models.Course,on_delete=models.CASCADE)
    enroll_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    parent_contact = models.TextField()
    
