from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def content_file_location(instance, filename):
    return '/'.join(['media/uploads', 'users', instance.user.username, 'images', filename])


class BlogContent(models.Model):
    post_title = models.CharField(max_length=150, blank=False, null=False)
    post_body = models.TextField(blank=False, null=False)
    youtube_link = models.URLField(max_length=200,  blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.post_title


