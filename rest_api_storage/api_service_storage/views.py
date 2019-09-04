from .serializers import ImageGetSerializer
from .models import Image
from rest_framework import generics, views
from rest_framework.response import Response


class ImageListFilterView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = []
        data_image = {}
        data = self.request.query_params
        serializer = ImageGetSerializer(data=data)
        serializer.is_valid()
        obj_images = Image.objects.filter(date=serializer.data['date'])
        for obj in obj_images:
            data_image.update({'obj_{}'.format(obj.id): {'date': obj.date_format, 'place': obj.place, 'path_to_image': obj.image.url}})
        return Response([data_image], status=200)