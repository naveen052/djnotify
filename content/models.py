from django.db import models
from tinymce import models as tinymce_models
from autoslug import AutoSlugField
# Create your models here.


class BlogContent(models.Model):
    post_title = models.CharField(max_length=150, blank=False, null=False)
    post_body = tinymce_models.HTMLField()
    youtube_link = models.URLField(max_length=200,  blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='uploads/', null=True)
    category = models.ForeignKey('content.Category')

    def get_file_path(self):
        return u'%s' % self.image

    def __unicode__(self):
        return self.post_title


class PostTypeVideo(models.Model):
    video_post_title = models.CharField(max_length=150, blank=False, null=False)
    video_post_url = models.URLField(max_length=200,  blank=True, null=True)
    video_post_media = models.FileField(upload_to='uploads/', null=False)

    def __unicode__(self):
        return self.video_post_title, self.video_post_url


class PostTypeAudio(models.Model):
    audio_post_title = models.CharField(max_length=150, blank=False, null=False)
    audio_post_url = models.URLField(max_length=200,  blank=True, null=True)
    audio_post_media = models.FileField(upload_to='uploads/', null=False)

    def __unicode__(self):
        return self.audio_post_title, self.audio_post_url


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='title', max_length=500)

    def __unicode__(self):
        return '%s' % self.title
