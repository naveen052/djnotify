from django.conf.urls import patterns, include, url
from django.contrib import admin
from content.views import PostList, VideoTypePostList, AudioTypePostList

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
                       url(r'^video/$', VideoTypePostList.as_view(), name='videos'),
                       url(r'^video/add/$',
                           'content.views.add_post_type_video',
                           name='add_video'),
                       url(r'^video/(?P<pk>[0-9]+)/edit/$',
                           'content.views.edit_video_post',
                           name='edit_video'),
                       url(r'^video/delete/(?P<pk>[0-9]+)$',
                           'content.views.delete_video_post',
                           name='delete_video'),
                       url(r'^audio/$', AudioTypePostList.as_view(), name='audio'),
                       url(r'^audio/add/$',
                           'content.views.add_post_type_audio',
                           name='add_audio'),
                       url(r'^audio/(?P<pk>[0-9]+)/edit/$',
                           'content.views.edit_audio_post',
                           name='edit_audio'),
                       url(r'^audio/delete/(?P<pk>[0-9]+)$',
                           'content.views.delete_audio_post',
                           name='delete_audio'),

)
