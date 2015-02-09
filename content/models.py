from django.db import models

# Create your models here.


class BlogContent(models.Model):
    post_title = models.CharField(max_length=150)
    post_body = models.CharField(max_length=1000)
    youtube_link = models.URLField(max_length=200)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.post_title