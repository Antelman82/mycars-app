from django.db import models

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

    def __str__(self):
        return self.name