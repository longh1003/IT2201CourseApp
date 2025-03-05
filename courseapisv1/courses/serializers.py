from rest_framework.serializers import ModelSerializer
from .models import Course, Category, Lesson


class BaseSerializer(ModelSerializer):

    # def to_representation(self, instance):
    #
    #     d = super().to_representation(instance)
    #     d['image'] = instance.image.url
    #     return d
    pass

class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_date', 'category', 'image', 'category_id']


class CategorySerializer(BaseSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'created_date', 'image']

class TagSerializer(BaseSerializer):
    pass


class LessonDetailsSerializer(LessonSerializer):
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']