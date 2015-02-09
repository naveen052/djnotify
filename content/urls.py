from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # ex: /polls/
                       url(r'^$', 'content.views.post_list', name='index'),
                       url(r'^post/$',
                           'content.views.add_content',
                           name='add_content'),
                       # ex: /polls/5/
)