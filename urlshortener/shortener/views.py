from urllib import response
from django.shortcuts import render, redirect
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
        "error": False
    }
    if request.method == "POST":
        context['submitted'] = True
        user_data = request.POST

        long_url = user_data['longurl']
        custom_name = user_data['custom_name']
        data = {}
        data['long_url'] = long_url
        data['short_url'] = request.build_absolute_uri() + custom_name
        try:
            obj = LongToShort(long_url=long_url, short_url=custom_name)
            obj.save()

            date = obj.date
            clicks = obj.clicks
            data['date'] = date
            data['clicks'] = clicks
            context['data'] = data
        except:
            context['submitted'] = False
            context['error'] = True

    return render(request, 'home.html', context)


def redirect_url(request, shorturl):
    row = LongToShort.objects.filter(short_url=shorturl)
    if len(row) == 0:
        return render(request, 'error.html')
    obj = row[0]
    long_url = obj.long_url
    obj.clicks += 1
    obj.save()
    return redirect(long_url)


def all_analytics(request):
    rows = LongToShort.objects.all()
    context = {
        "rows": rows
    }
    print(rows)
    return render(request, 'all_analytics.html', context)
