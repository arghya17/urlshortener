from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from .models import LongToShort


def example_view(request, name):
    # name slug variable
    data = {
        'name': name
    }
    return render(request, 'index.html', data)
# Create your views here.


def task_view(request):
    data = {
        'task': 'django workshop'
    }
    return render(request, 'task.html', data)


def shorten_url(request):
    context = {
        "submitted": False,
    }
    if request.method == "POST":
        context['submitted'] = True
        user_data = request.POST

        long_url = user_data['longurl']
        custom_name = user_data['custom_name']
        data = {}
        data['long_url'] = long_url
        data['short_url'] = request.build_absolute_uri() + custom_name

        obj = LongToShort(long_url=long_url, short_url=custom_name)
        obj.save()

        date = obj.date
        clicks = obj.clicks
        data['date'] = date
        data['clicks'] = clicks
        context['data'] = data
        print(long_url, custom_name)
    return render(request, 'home.html', context)
