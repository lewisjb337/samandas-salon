from django.shortcuts import render
from .models import service

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services = service.objects.all()

    context = {
        "services": services,
    }

    return render(request, 'services.html', context)

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    services = service.objects.all()

    context = {
        "services": services,
    }

    return render(request, 'contact.html', context)