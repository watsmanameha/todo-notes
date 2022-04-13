import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from django.contrib.auth.models import User
from .views import UserModelViewSet
from .models import User
from todo.models import Project
from todo.views import ProjectModelViewSet


class TestUserModelViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self, path='/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = User.objects.create(username='test_admin', firstname='me')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@mail.ru', 'admin123')
        client.login(username='admin', password='admin123')
        response = client.put(f'/api/users/{user.id}/'), {'username': 'non_admin', 'firstname': 'not_me'}
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, 'non_admin')
        self.assertEqual(user.firstname, 'not_me')
        client.logout()


class TestProjectViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_project_edit_admin(self):
    #     user = User.objects.create(username='Pushkin1', firstname='Alex')
    #     project = Project.objects.create(project_name='Proj1', user=user)
    #     admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
    #     self.client.login(username='admin', password='admin123')
    #     response = self.client.put(f'/api/projects/{project.id}/', {'project_name': 'Proj2', 'user': project.users.od})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Project.objects.get(id=project.id)
    #     self.assertEqual(project.project_name, 'Proj1')
