from django.db import models

# Create your models here.


def content_file_location(instance, filename):
    return '/'.join(['media/uploads', 'users', instance.user.username, 'images', filename])


class BlogContent(models.Model):
    post_title = models.CharField(max_length=150, blank=False, null=False)
    post_body = models.TextField(blank=False, null=False)
    youtube_link = models.URLField(max_length=200,  blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to=content_file_location, max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            this = BlogContent.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete(save=False)
        except:
            pass

        super(BlogContent, self).save(*args, **kwargs)



    def __unicode__(self):
        return self.post_title


