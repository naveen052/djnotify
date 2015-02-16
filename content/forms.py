from django import forms
from content.models import BlogContent, PostTypeVideo


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogContent

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['post_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['post_body'].widget.attrs.update({'class': 'form-control'})
        self.fields['youtube_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class PostTypeVideoForm(forms.ModelForm):
    class Meta:
        model = PostTypeVideo

    def __init__(self, *args, **kwargs):
        super(PostTypeVideoForm, self).__init__(*args, **kwargs)
        self.fields['video_post_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['video_post_url'].widget.attrs.update({'class': 'form-control'})
        self.fields['video_post_media'].widget.attrs.update({'class': 'form-control'})