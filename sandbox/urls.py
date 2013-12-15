from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Examples:
    #url(r'^$', 'sandbox.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/$', 'books.views.index'),
    url(r'^dogpics/$', 'dogpics.views.albums_view'),
    url(r'^dogpics/album/(?P<album_id>\d+)$', 'dogpics.views.album_view'),

)
