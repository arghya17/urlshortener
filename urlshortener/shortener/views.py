from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


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
    if request.method == "POST":
        user_data = request.POST

        long_url = user_data['longurl']
        custom_name = user_data['custom_name']

        print(long_url, custom_name)

    return render(request, 'home.html')