from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .serializers import CourseSerializer, CategorySerializer, LessonSerializer, LessonDetailsSerializer
from .models import Course, Category, Lesson


class CategoryViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.queryset

        q = self.request.query_params.get('q')
        if q:
            query = query.filter(subject__contains=q)
        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            query = query.filter(category=cate_id)
        return query

    #bth2 bai 3
    # courses/{course_id}/lessons/?q=
    #{course_id} = pk
    @action(methods=['get'], url_path='lessons', detail=True)
    def get_lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)
        return Response(serializers.LessonSerializer(lessons, many=True).data)


class LessonViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonDetailsSerializer