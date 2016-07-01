'''Shorty URLs'''
from django.conf.urls import url, include

from . import views
from . import app_settings
from .api.v1 import api as v1_api

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', views.do_redirect, name='redirect_base'),
    url(r'^(?P<slug>[-_\w]+)/?$', views.do_redirect, name='redirect'),
]

if app_settings.ADMIN_ENABLED:
    urlpatterns = [
        url(r'^admin/$', views.home, name='home'),
        url(r'^admin/delete/$', views.delete, name='delete'),
    ] + urlpatterns
