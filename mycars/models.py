from django.db import models

class Year(models.Model):
    model_year = models.TextField()

    def __str__(self):
        return self.model_year

class ModelType(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='models')
    name = models.TextField(max_length=100, default='no model name')
    trim = models.TextField(max_length=200, null=True)
    description = models.TextField(default='no model description')
    image_file = models.ImageField(upload_to='images/', null=True)
    image_url = models.TextField(max_length=200, null=True)


    def __str__(self):
        return self.name