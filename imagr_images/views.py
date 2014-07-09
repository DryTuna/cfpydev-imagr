from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def photos(request):
    return render(request, 'imagr_images/photos.html')
