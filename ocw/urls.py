from django.conf.urls import patterns, include, url

from os.path import join, abspath, dirname

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   #patterns('',
    # Examples:
    # url(r'^$', 'ocw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('fileupload.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': join(abspath(dirname(__file__)), 'media')}),
]
#)
