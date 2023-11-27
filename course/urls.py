from django.urls import path
from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentsListAPIView, SubscriptionCreateAPIView, SubscriptionListAPIView, \
    SubscriptionDestroyAPIView, PaymentCreateAPIVIew

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('payment/create/', PaymentCreateAPIVIew.as_view(), name='payment_create'),
                  path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
                  path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
                  path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
                  path('subscription/delete/<int:pk>', SubscriptionDestroyAPIView.as_view(),
                       name='subscription_delete'),

              ] + router.urls
