from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', question.views.index, name='index'),
    url(r'^db', question.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
