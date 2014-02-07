from django.conf.urls import patterns, include, url

from tastypie.api import api
from api.resources import NoteResource

v1_api = Api(api_name='v1')
v1_api.register(NoteResource())

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('notes.urls')),
    (r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
