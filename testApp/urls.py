
from django.contrib import admin
from testApp import views
from django.urls import path, include

urlpatterns = [
    path('',views.main_page)
]
