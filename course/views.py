from course import models, serializers
from rest_framework import viewsets


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()