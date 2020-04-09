from django.db import models
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Year(models.Model):
    model_year = models.TextField()

    def __str__(self):
        return self.model_year

class ModelType(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='models')
    make = models.TextField(max_length=100, null=True)
    name = models.TextField(max_length=100)
    trim = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    image_file = models.ImageField(upload_to='images/', null=True, blank=True)
    image_url = models.TextField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
        self.image_file = self.compressImage(self.image_file)
    super(ModelType, self).save(*args, **kwargs)

    def compressImage(self, image_file):
        imageTemproary = Image.open(image_file)
    outputIoStream = BytesIO()
    imageTemproaryResized = imageTemproary.resize( (300,300) ) 
    imageTemproary.save(outputIoStream , format='JPEG', quality=20)
    outputIoStream.seek(0)
    image_file = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % modeltype.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    return image_file

    def __str__(self):
        return self.name