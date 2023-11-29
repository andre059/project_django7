from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.models import Course, Lesson, Subscription
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
            {'id': 1, 'lesson_count': 0, 'lessons': [], 'title': 'Test', 'picture': None, 'description': 'Test'}
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
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 2, 'lesson_count': 0, 'lessons': [],
                                                                      'title': 'List test', 'picture': None,
                                                                      'description': 'List test'}]}
        )


class EducationLessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='Test1234!', is_staff=True, is_superuser=True)
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

        response = self.client.get(path='/lesson/')

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 4,
                        "title": "lesson test",
                        "duration": None,
                        "picture": None,
                        "link_video": "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k",
                        "course": 5
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создание урока"""

        data = {
            "title": "create test2",
            "link_video": "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k"
        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_retrieve_lesson(self):
        """Тестирование вывода списка одного урока"""

        response = self.client.get(
            f'/lesson/{self.lesson.id}/'
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.id,
                'title': 'lesson test',
                'duration': None,
                'picture': None,
                'link_video': "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k",
                'course': self.course.id,
            }
        )

    def test_update_lesson(self):
        """Тестирование редактирование урока"""

        data = {
            "title": "update test",
        }

        response = self.client.patch(
            f'/lesson/update/{self.lesson.id}/',
            data=data,
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.id,
                'title': 'update test',
                'duration': None,
                'picture': None,
                'link_video': "https://youtu.be/TV7xiGwprGw?si=JijksZru_r-4y18k",
                'course': self.course.id,
            }
        )

    def test_destroy_lesson(self):
        """Тестирование удаление урока"""

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/'
        )

        # print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


# def tearDown(self):
#     Course.objects.all().delete()
#     Lesson.objects.all().delete()
#     Subscription.objects.all().delete()
