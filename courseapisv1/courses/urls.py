
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('course', views.CourseViewSet, basename='course')
router.register('category', views.CategoryViewSet, basename='category')
router.register('lesson', views.LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls))
]