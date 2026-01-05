from django import forms
from .models import Service

class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'title',
            'description',
            'price',
            'delivery_days',
            'category',
            'skills',
        ]
