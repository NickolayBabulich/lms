from rest_framework import serializers
from course.models import Course, Lesson, Payments, Subscription
from course.validators import LinkToVideoValidator
from users.models import User
from rest_framework.relations import SlugRelatedField


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            LinkToVideoValidator(field='link_to_video')
        ]


class CourseSerializer(serializers.ModelSerializer):
    # Кастомизация сериализатора подгрузкой данных из связанной модели (количество уроков в курсе)
    # number_of_lessons = serializers.IntegerField(source='lesson.count')

    # Кастомизация сериализатора добавлением динамического поля (количество уроков в курсе)
    number_of_lessons = serializers.SerializerMethodField()

    lessons = LessonSerializer(source='lesson', many=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, instance):
        return Subscription.objects.filter(course=instance, user=self.context['request'].user).exists()

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


class SubscriptionSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Subscription
        fields = '__all__'