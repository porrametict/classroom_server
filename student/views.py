from django_filters.rest_framework import DjangoFilterBackend
from student import serializers, models
from rest_framework import viewsets, filters


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializers
    queryset = models.Student.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['course_id']
