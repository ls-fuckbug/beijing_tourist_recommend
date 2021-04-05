from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

from django.urls import path, include
from . import view

urlpatterns = [
    path('travelhome',view.travelHome),
    path('404.html',view.error404),
    path('about.html',view.about),
    path('blog.html', view.blog),
    path('blog-single.html', view.blog_single),
    path('contact.html', view.contact),
    path('gallery.html', view.gallery),
    path('icons.html', view.icons),
    path('select/', view.select),
    path('home/', view.mainWindow),
    path('home/ajax/', view.getArgx),
]


