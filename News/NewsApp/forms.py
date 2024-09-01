from django import forms
from . import models

class CustomForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'content', 'author','status', 'created_at')