from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        IntegerField,
                                        CharField,
                                        Serializer)
from .models import Image


class ImageGetSerializer(Serializer):
    date = CharField(max_length=20, default=None)
    size = IntegerField(default=0)


class ImageListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
                                   lookup_field='id',
                                   view_name='image_detail'
    )

    class Meta:
        model = Image
        fields = ('date', 'place', 'url')


class ImageDetailSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('date', 'place', 'url')
