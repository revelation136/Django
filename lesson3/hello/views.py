from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    # adding html file to view, this is templating
    return render(request, "hello/index.html")


# adding dynamic response
def greet(request, name):
    return render(request, "hello/greet.html",
                  {"name": name.capitalize()})

