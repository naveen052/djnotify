from django import forms
from content.models import BlogContent


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogContent

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['post_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['post_body'].widget.attrs.update({'class': 'form-control'})
        self.fields['post_title'].widget.attrs.update({'class': 'form-control'})