from django.shortcuts import render, HttpResponse
from .models import projects

# Create your views here.

def portfolio(request):
    projs = projects.objects.all()
    return render(request, "portfolio.html", {"project": projs})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")