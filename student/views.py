from django.shortcuts import render
from student import serializers, models
from rest_framework import viewsets


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializers
    queryset = models.Student.objects.all().order_by('-id')
