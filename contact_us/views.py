from django.shortcuts import render

# Create your views here.
def contact_us(request):
    """ A view to render out the index.html"""
    return render(request, 'contact_us/contact_us.html')