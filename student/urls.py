from student import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls))
] 