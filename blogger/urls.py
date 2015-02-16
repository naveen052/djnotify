from django.conf.urls import patterns, include, url
from django.contrib import admin
from content.views import PostList

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'blogger.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       (r'^tinymce/', include('tinymce.urls')),
                       url(r'^$', PostList.as_view(), name='index'),
                       url(r'^addpost/$',
                           'content.views.add_content',
                           name='add_content'),
                       url(r'^(?P<pk>[0-9]+)/edit/$',
                           'content.views.edit_post',
                           name='edit'),
                       url(r'^delete/(?P<pk>[0-9]+)$',
                           'content.views.delete_post',
                           name='delete'),
)
