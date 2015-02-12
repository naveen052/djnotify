from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'blogger.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'content.views.post_list', name='index'),
                       url(r'^addpost/$',
                           'content.views.add_content',
                           name='add_content'),
)
