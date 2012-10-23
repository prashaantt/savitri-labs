from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from hellodjango.views import hello, current_datetime, nlp, stats, search, compare
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^nlp/$', nlp),
    (r'^stats/$', stats),
    ('^compare/$',compare),
    (r'^search/$',search),
    (r'^admin/', include(admin.site.urls)),
)
