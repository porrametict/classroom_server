from django.shortcuts import render
from course import models, serializers
from rest_framework import viewsets, status
from rest_framework.response import Response


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()

    def create(self, request, *args, **kwargs):
        teaching_period_serializer = serializers.TeachingPeriodSerializer(data=request.data)
        if teaching_period_serializer.is_valid():
            teaching_period_serializer.save()
            new_data = request.data
            # new_data = new_data.dict()   # fix => AttributeError: 'dict' object has no attribute 'dict'
            new_data['teaching_period'] = teaching_period_serializer.data['id']
            course_data = self.save_corse(new_data)
            print(course_data)
            return Response(course_data, status=status.HTTP_200_OK)
        else:
            return Response(teaching_period_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_corse(self, data):
        course_serializer = serializers.CourseSerializer(data=data)
        if course_serializer.is_valid():
            course_serializer.save()
            return course_serializer.data
        else:
            return course_serializer.errors
