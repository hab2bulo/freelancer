from django import forms
from .models import Project

class ProjectCreateForm(forms.ModelForm):
    """
    Client project joylash uchun form
    """
    class Meta:
        model = Project
        fields = ['title', 'description', 'budget', 'category']
