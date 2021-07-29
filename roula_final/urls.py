from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('', include('theblog.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('locations/', include('locations.urls')),
    path('contact_form/', include('contact_form.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
