from django.urls import path, include
from django.conf.urls import url
from . import view

urlpatterns = [
    path('test/',include('testApp.urls')),
    path('hello1/', view.runoob),
]
