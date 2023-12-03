import datetime
from celery import shared_task
from django.utils import timezone
from course.models import Subscription, Lesson
from users.models import User


@shared_task
def check_add_lesson(course_id, lesson_id):
    print(
        f'Добавлен новый урок {Lesson.objects.get(pk=lesson_id)} в курс {Subscription.objects.filter(course_id=course_id)}')


@shared_task
def check_active_user():
    now = datetime.datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if now - user.last_login > datetime.timedelta(days=30):
                user.is_active = False
                user.save()
                print('Пользователь был деактивирован по прошествии 30 дней с момента последнего входа')
