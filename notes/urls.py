from django.conf.urls import patterns, include, url




urlpatterns = patterns('',

    url(r'^$', 'notes.views.index'),
    url(r'^test', 'notes.views.test'),

)