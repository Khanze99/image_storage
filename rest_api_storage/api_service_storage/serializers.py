from rest_framework.serializers import (ModelSerializer,
                                        ImageField,
                                        IntegerField,
                                        CharField,
                                        Serializer,
                                        HyperlinkedIdentityField)
from .models import Image


class ImageGetSerializer(Serializer):
    date = CharField(max_length=20, default=None)
    size = IntegerField(default=0)


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'date', 'place', 'img')


class ImageSaveStorageSerializer(Serializer):
    img = ImageField()
    place = CharField(max_length=50)
