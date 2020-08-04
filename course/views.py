from course import models, serializers
from rest_framework import viewsets, generics


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all().order_by('-id')


class CourseListAPIView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all().order_by('-id')
    pagination_class = None
