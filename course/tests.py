from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from course.models import Lesson, User, Course, Subscription


class LessonTestCase(APITestCase):
    """ Основные настройки """
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.test', password='1'
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='test'
        )
        self.lesson = Lesson.objects.create(
            title='test',
            description='test',
            course=self.course,
            owner=self.user,
        )

    def test_get_list_lesson(self):
        """ Тест получения списка уроков """
        data_lesson = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.lesson.id,
                    'title': self.lesson.title,
                    'description': self.lesson.description,
                    'preview': self.lesson.preview,
                    'link_to_video': self.lesson.link_to_video,
                    'course': self.lesson.course.id,
                    'owner': self.user.id
                }
            ]
        }
        response = self.client.get(reverse('course:lesson_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data_lesson)

    def test_lesson_create(self):
        """ Тест создания урока """
        data = {
            'title': 'testttrr',
            'description': 'testtrtr',
            'link_to_video': 'https://www.youtube.com/watch?v=NjJx6B5De8g'
        }

        response = self.client.post(reverse("course:lesson_create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_retrieve(self):
        """ Тест получения информации об одном уроке """
        data = {'id': self.lesson.id,
                'title': self.lesson.title,
                'description': self.lesson.description,
                'preview': self.lesson.preview,
                'link_to_video': self.lesson.link_to_video,
                'course': self.lesson.course.id,
                'owner': self.user.id}
        response = self.client.get(reverse('course:lesson_get', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
        print(response.json())

    def test_lesson_update(self):
        """ Тест обновления информации урока """
        data = {
            'title': 'tes13',
            'description': 'test13',
            'link_to_video': 'https://www.youtube.com/watch?v=NjJx6B5De8g',
            'course': self.lesson.course.id,
        }

        response = self.client.put(reverse('course:lesson_update', args=[self.lesson.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())
        self.assertEqual(response.json(),
                         {'id': self.lesson.id, 'title': data['title'], 'description': data['description'],
                          'preview': self.lesson.preview,
                          'link_to_video': data['link_to_video'], 'course': self.lesson.course.id,
                          'owner': self.user.id})

    def test_lesson_delete(self):
        """ Тест удаление урока """
        response = self.client.delete(reverse('course:lesson_delete', args=[self.lesson.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)


class SubscriptionAPITestCase(APITestCase):
    """ Основные настройки тестов подписки """
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.test', password='1'
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='test'
        )
        self.lesson = Lesson.objects.create(
            title='test',
            description='test',
            course=self.course,
            owner=self.user,
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_subscription_list(self):
        """ Тест получения списка подписки """
        response = self.client.get(reverse('course:subscription_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         [
                             {'id': self.subscription.id,
                              'user': self.subscription.user.email,
                              'course': self.subscription.course.title,
                              }
                         ])

    def test_subscription_delete(self):
        """ Тест удаления подписки """
        response = self.client.delete(reverse('course:subscription_delete', args=[self.subscription.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
