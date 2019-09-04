from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        IntegerField,
                                        CharField,
                                        Serializer)
from .models import Image


class ImageGetSerializer(Serializer):
    date = CharField(max_length=20)
    size = IntegerField(default=0)
