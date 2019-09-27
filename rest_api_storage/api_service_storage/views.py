from .serializers import ImageSerializer
from .models import Image
from rest_framework import generics, views
from rest_framework.response import Response
from django.shortcuts import redirect


def redirect_service(request):
    return redirect('info')


class InfoService(views.APIView):
    def get(self, request):
        return Response({'get': 'service/photos/', 'post': 'service/photo/'}, status=200)


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
        obj = Image.objects.create(img=request.FILES['img'], place=data['place'])
        return Response(status=200)
