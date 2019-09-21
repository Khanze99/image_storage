from django.test import TestCase
from rest_framework.test import APIRequestFactory
from datetime import datetime
import os

# ------------------------- request get to http://localhost/
factory = APIRequestFactory()
request_to_info_redirect = factory.get('/')

# ------------------------- request post to http://localhost/service/photo/
file = open('api_service_storage/test/test_image_1.jpg', mode='rb')
data = {'place': 'nissan'}
files = {'img': file}
post_request = factory.post('/service/photo/', files=files, data=data)
file.close()

file_2 = open('api_service_storage/test/test_image_2.jpg', mode='rb')
data = {'place': 'human'}
files = {"img": file_2}
post_request_2 = factory.post('/service/photo/', files=files, data=data)
file_2.close()


# ------------------------- request get to http://localhost/service/photos/

get_request = factory.get('/service/photos/')


# ------------------------- request get to http://localhost/service/photos/ with filter time

date = datetime.now().date().strftime('%Y-%m-%d')
get_request_filter = factory.get('/service/photos/', params={'date': date})



