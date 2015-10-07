from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'django_start.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls))
]
