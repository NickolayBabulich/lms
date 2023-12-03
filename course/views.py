from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from course.models import Course, Lesson, Payments, Subscription

from course.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer, \
    PaymentCreateSerializer
from course.permissions import IsNotModer, IsNotModerForView
from course.paginators import CoursePaginator, LessonPaginator
from course.tasks import check_add_lesson

from course.services import get_session_with_pay


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsNotModerForView]
    pagination_class = CoursePaginator

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)
        else:
            return Course.objects.all()

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsNotModer]

    def perform_create(self, serializer):

        course_id = serializer.save(owner=self.request.user).course.id
        lesson_id = serializer.save().id
        check_add_lesson.delay(course_id, lesson_id)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = LessonPaginator

    # permission_classes = [AllowAny]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Lesson.objects.filter(owner=self.request.user)
        else:
            return Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsNotModer]


class PaymentCreateAPIVIew(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.session = get_session_with_pay(payment).id
        payment.save()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payment_day',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        subscriptions = Subscription.objects.filter(user=self.request.user)
        for subscription in subscriptions:
            if subscription.course.title == request.data.get('course'):
                raise PermissionError('Вы уже подписаны на этот курс')
        return super().create(request, *args, **kwargs)


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
