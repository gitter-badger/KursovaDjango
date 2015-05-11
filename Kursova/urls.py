from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.dictionary.containers'),
    url(r'^dictionary/container', 'app.dictionary.container'),

    url(r'^login$', 'app.views.login_form'),
    url(r'^register', 'app.views.register'),
    url(r'^logout', 'app.views.log_out'),

    url(r'^dictionary/regions', 'app.dictionary.regions'),
    url(r'^dictionary/region', 'app.dictionary.region'),

    url(r'^dictionary/distincts', 'app.dictionary.disctincts'),
    url(r'^dictionary/distinct', 'app.dictionary.distinct'),

    url(r'^dictionary/cities', 'app.dictionary.cities'),
    url(r'^dictionary/city', 'app.dictionary.city'),

    url(r'^dictionary/places', 'app.dictionary.places'),
    url(r'^dictionary/place', 'app.dictionary.place'),

    url(r'^dictionary/owners', 'app.dictionary.owners'),
    url(r'^dictionary/owner', 'app.dictionary.owner'),

    url(r'^dictionary/marchents', 'app.dictionary.marchents'),
    url(r'^dictionary/marchent', 'app.dictionary.marchent'),

    url(r'^admin/', include(admin.site.urls)),
)
