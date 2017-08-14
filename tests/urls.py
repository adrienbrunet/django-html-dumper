# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from html_dumper.urls import urlpatterns as html_dumper_urls

urlpatterns = [
    url(r'^', include(html_dumper_urls, namespace='html_dumper')),
]
