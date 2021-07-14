from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Message


# Create your views here.
def contact_us(request):
    """ A view to render out the index.html"""
    return render(request, 'contact_us/contact_us.html')


class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact'    

    def form_valid(self, form):
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        message = Message(email=email, message=message)
        message.save()
        
        messages.success(self.request, 'Message received 👽')
        
        return super().form_valid(form)