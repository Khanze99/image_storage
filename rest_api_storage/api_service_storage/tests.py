from rest_framework.test import APIRequestFactory, APITestCase, URLPatternsTestCase
from rest_framework import status
from django.urls import reverse, path, include
from api_service_storage.models import Image


class Test(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('rest_api_storage.urls'))
    ]

    def test_post_photo(self):
        url = reverse('photo')
        image = open('./api_service_storage/test/test_image_1.jpg', mode="rb")
        post_data = {'place': 'test1', 'img': image}
        response = self.client.post(url, post_data)
        image.close()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.get(id=1).place, 'test1')

    def test_info(self):
        url = reverse('info')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'get': 'service/photos/', 'post': 'service/photo/'})

    def test_list(self):
        url = reverse('photos')
        response = self.client.get(url)
        self.assertEqual(response.json(), [])
