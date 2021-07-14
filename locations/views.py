# Create your views here.
from django.shortcuts import render


def index(request):
    """ A view to render out the locations.html"""
    return render(request, 'locations/locations.html')