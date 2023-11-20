from rest_framework import serializers
from course.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # Кастомизация сериализатора подгрузкой данных из связанной модели (количество уроков в курсе)
    # number_of_lessons = serializers.IntegerField(source='lesson.count')

    # Кастомизация сериализатора добавлением динамического поля (количество уроков в курсе)
    number_of_lessons = serializers.SerializerMethodField()

    lessons = LessonSerializer(source='lesson', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_number_of_lessons(instance):
        return instance.lesson.count()


class PaymentsSerializer(serializers.ModelSerializer):
    payment_user = serializers.CharField(source='user.email')

    class Meta:
        model = Payments
        fields = '__all__'
