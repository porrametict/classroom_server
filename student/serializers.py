from rest_framework import serializers
from student import models

class StudentSerializers(serializers.ModelSerializer):
    class Meta : 
         fields = '__all__'
         model = models.Student