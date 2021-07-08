from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to render out the index.html"""
    return render(request, 'home/index.html')