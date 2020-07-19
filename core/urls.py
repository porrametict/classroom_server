from django.urls import path, include
from rest_framework import routers
from core import views as core_views

router = routers.DefaultRouter()
router.register('user-profile', core_views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
