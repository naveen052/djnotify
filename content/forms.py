from django import forms
from content.models import BlogContent


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogContent