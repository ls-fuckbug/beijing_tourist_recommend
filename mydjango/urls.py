from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

from django.urls import path, include
from . import view

urlpatterns = [
    path('', view.travelHome),
    path('travelhome',view.travelHome),
    path('404.html',view.error404),
    path('about.html',view.about),
    path('blog.html', view.blog),
    path('blog-single.html', view.blog_single),
    path('contact.html', view.contact),
    path('gallery.html', view.gallery),
    path('spot.html', view.spot_choose),
    path('route.html', view.route_show),
    path('reco', view.reco),


]


