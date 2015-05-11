# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.forms import TypeForm, RegionForm, DistinctForm, CityForm, PlaceForm, OwnerForm, MarchentForm, ContainerForm
from core.models import Container, Region, Distinct, City, Place, Owner, Marchent, Type

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'app.dictionary.get_list', {'model': Container, 'template': 'containers.html'}),

                       url(r'^login$', 'app.views.login_form'),
                       url(r'^register', 'app.views.register'),
                       url(r'^logout', 'app.views.log_out'),

                       url(r'^dictionary/regions', 'app.dictionary.get_list',
                           {'model': Region, 'template': 'regions.html'}),

                       url(r'^dictionary/distincts', 'app.dictionary.get_list',
                           {'model': Distinct, 'template': 'disctincts.html'}),

                       url(r'^dictionary/cities', 'app.dictionary.get_list',
                           {'model': City, 'template': 'cities.html'}),

                       url(r'^dictionary/places', 'app.dictionary.get_list',
                           {'model': Place, 'template': 'places.html'}),

                       url(r'^dictionary/owners', 'app.dictionary.get_list',
                           {'model': Owner, 'template': 'owners.html'}),

                       url(r'^dictionary/marchents', 'app.dictionary.get_list',
                           {'model': Marchent, 'template': 'marchents.html'}),

                       url(r'^dictionary/types', 'app.dictionary.get_list', {'model': Type, 'template': 'types.html'}),

                       url(r'^dictionary/type', 'app.dictionary.get_form',
                           {'model': Type, 'name': 'Новий тип', 'model_form': TypeForm, 'back': 'types',
                            'now': 'type'}),

                       url(r'^dictionary/region', 'app.dictionary.get_form',
                           {'model': Region, 'name': 'Нова область', 'model_form': RegionForm, 'back': 'regions',
                            'now': 'region'}),

                       url(r'^dictionary/distinct', 'app.dictionary.get_form',
                           {'model': Distinct, 'name': 'Новий район', 'model_form': DistinctForm, 'back': 'distincts',
                            'now': 'distinct'}),

                       url(r'^dictionary/city', 'app.dictionary.get_form',
                           {'model': City, 'name': 'Нове місто', 'model_form': CityForm, 'back': 'cities',
                            'now': 'city'}),

                       url(r'^dictionary/place', 'app.dictionary.get_form',
                           {'model': Place, 'name': 'Нове місце', 'model_form': PlaceForm, 'back': 'places',
                            'now': 'place'}),

                       url(r'^dictionary/owner', 'app.dictionary.get_form',
                           {'model': Owner, 'name': 'Новий власник', 'model_form': OwnerForm, 'back': 'owners',
                            'now': 'owner'}),

                       url(r'^dictionary/marchent', 'app.dictionary.get_form',
                           {'model': Marchent, 'name': 'Новий орендар', 'model_form': MarchentForm, 'back': 'marchents',
                            'now': 'marchent'}),

                       url(r'^dictionary/container', 'app.dictionary.get_form',
                           {'model': Container, 'name': 'Новий контейнер', 'model_form': ContainerForm, 'back': '../',
                            'now': 'container'}),
                       url(r'^admin/', include(admin.site.urls)),
                       )
