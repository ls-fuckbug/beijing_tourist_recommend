from django.urls import path, include
from django.conf.urls import url
from . import view

urlpatterns = [
    path('test/',include('testApp.urls')),
    url (r'^get\.html$', view.get_html),
    url (r'^get$', view.get),
    url (r'^post\.html$', view.post_html),
    url (r'^post$', view.post),
]
