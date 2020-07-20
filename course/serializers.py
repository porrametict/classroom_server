from course import models
from rest_framework import serializers

class  TeachingPeriodSerializer(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = models.TeachingPeriod
    
class CourseSerializer(serializers.ModelSerializer):
    teaching_period_data = TeachingPeriodSerializer(read_only=True,source='teaching_period')
    class Meta :
        fields = '__all__'
        model = models.Course
    
