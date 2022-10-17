from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('example/<slug:name>', example_view),
    path('task/', task_view),
    path('shorten/', shorten_url)
]
