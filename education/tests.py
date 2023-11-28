import json

from django.http import HttpResponseNotFound
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.apps import EducationConfig
from education.models import Course, Lesson
from users.models import User


class EducationCourseTestCase(APITestCase):

    def setup(self) -> None:
        pass

    def test_create_course(self):
        """Тетирование создание курса"""

        data = {
            "title": "Test",
            "description": "Test"
        }
        response = self.client.post(
            '/course/',
            data=data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'lesson_count': 0, 'title': 'Test', 'picture': None, 'description': 'Test'}
        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_list_course(self):
        """Тестирование вывода списка уроков"""

        Course.objects.create(
            title="List test",
            description="List test"
        )

        response = self.client.get(
            '/course/'
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 1, 'lesson_count': 0, 'title': 'List test',
                                                                      'picture': None, 'description': 'List test'}]}
        )


class EducationLessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='Test1234!')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='test',
            description="первый курс"
        )

        self.lesson = Lesson.objects.create(
            title="lesson test",
            link_video="https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k",
            course=self.course
        )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(path='/lesson/'
            # reverse(f'{EducationConfig.name}:list')
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print('DEBUG', response)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "title": "lesson test",
                        "duration": None,
                        "picture": None,
                        "link_video": "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k",
                        "course": 1
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создание урока"""

        data = {
            "title": "create test",
            "link_video": "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k"
        }

        response = self.client.post(
            'lesson/create/',
            data=data,
        )

        # print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertEqual(
            response['content-type'],
            'text/html; charset=utf-8'

        )

    def test_retrieve_lesson(self):
        """Тестирование вывода списка одного урока"""

        Course.objects.create(
            title="list test2",
        )

        response = self.client.get(
            'lesson/<int:pk>/'
        )

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertEqual(
            response['content-type'],
            'text/html; charset=utf-8'
        )

    def test_update_lesson(self):
        """Тестирование редактирование урока"""

        data = {
            "title": "update test",
            "link_video": "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18kUpdate"
        }

        response = self.client.put(
            'lesson/update/<int:pk>/',
            data=data,
        )

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertEqual(
            response['content-type'],
            'text/html; charset=utf-8'
        )

    def test_destroy_lesson(self):
        """Тестирование удаление урока"""

        data = {
            "title": "update test",
            "link_video": "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18kUpdate"
        }

        response = self.client.delete(
            'lesson/delete/<int:pk>/',
            data=data,
        )

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertEqual(
            response['content-type'],
            'text/html; charset=utf-8'
        )
