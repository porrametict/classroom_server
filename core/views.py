from rest_framework import viewsets, status
from rest_framework.response import Response
from core import models as core_models, serializers as core_serializers


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = core_serializers.UserProfile
    queryset = core_models.UserProfile.objects.all()
