from django.shortcuts import render


def index(request):
    """ A view to render out the index.html"""
    return render(request, 'contact_form/contact.html')