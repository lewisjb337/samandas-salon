from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
]

handler404 = "samandas_salon_app.views.page_not_found_view"

