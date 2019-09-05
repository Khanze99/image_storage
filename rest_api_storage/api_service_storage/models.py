from django.db import models
from django.utils import timezone
from uuid import uuid4


def upload_image(instance, filename):
    return 'images/{}'.format(filename)


class Image(models.Model):
    place = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        if self.place:
            return self.place
        else:
            str_id = str(self.id)
            return str_id

    @property
    def date_format(self):
        self.date = self.date.strftime("%Y-%m-%d")
        return self.date


