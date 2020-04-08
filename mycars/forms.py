from django import forms
from .models import Year, ModelType

class YearForm(forms.ModelForm):

    class Meta:
        model = Year
        fields = ('model_year',)

class ModelTypeForm(forms.ModelForm):

    class Meta:
        model = ModelType
        fields = ('year', 'make', 'name', 'trim', 'description', 'image_url', 'image_file',)