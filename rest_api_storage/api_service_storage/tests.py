from rest_framework.test import APIRequestFactory, APITestCase, URLPatternsTestCase
from rest_framework import status
from django.urls import reverse, path, include
from api_service_storage.models import Image


class Test(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('rest_api_storage.urls'))
    ]

    def test_info(self):
        url = reverse('info')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'get': 'service/photos/', 'post': 'service/photo/'})

    def test_list(self):
        url = reverse('photos')
        response = self.client.get(url)
        self.assertEqual(response.json(), [])
