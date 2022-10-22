from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('example/<slug:name>', example_view),
    path('task/', task_view),
    path('', shorten_url),
    path('all_analytics', all_analytics),
    path('<slug:shorturl>', redirect_url),
]
# slug very important feature
