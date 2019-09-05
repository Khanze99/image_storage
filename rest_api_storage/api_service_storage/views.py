from .serializers import ImageGetSerializer, ImageSerializer
from .models import Image
from rest_framework import generics, views
from rest_framework.response import Response


class ImagesListView(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        filter = self.request.query_params
        queryset = Image.objects.all()
        if 'date' in filter:
            queryset = queryset.filter(date=filter.get('date'))
        return queryset


class ImageDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageSaveStorage(views.APIView):
    def post(self, request):
        data = request.data
        obj = Image.objects.create(image=request.FILES['image'], place=data['place'])
        return Response(status=200)



