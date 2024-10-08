from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class ImageGroup(models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.ForeignKey(
        ImageGroup,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name1 = models.CharField(
        max_length=20,
        null=True,
    )
    age = models.CharField(
        max_length=20,
        null=True,
    )
    height = models.CharField(
        max_length=20,
        null=True,
    )
    nationality = models.CharField(
        max_length=20,
        null=True,
    )
    image = CloudinaryField(
        folder="media/",  # Specify the folder name here
        overwrite=True,  # Optional: allows overwriting existing files with the same name
        resource_type="image",  # Optional: specify resource type (image, raw, video)
        blank=True,
        null=True,
    )

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " "
        return url
