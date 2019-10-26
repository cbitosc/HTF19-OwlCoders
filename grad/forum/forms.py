from django import forms
from django.db import models
from .models import Post
class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'article',
            'image',
        )

class EditPostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'image',
        )