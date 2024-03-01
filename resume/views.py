from django.shortcuts import render, HttpResponse
from .models import projects, profile, summary, schools, skill

# Create your views here.

def portfolio(request):
    projs = projects.objects.all()
    return render(request, "portfolio.html", {"project": projs})


def about(request):
    prof = profile.objects.all()
    summ = summary.objects.all()
    schol = schools.objects.all()
    skills = skill.objects.all()
    return render(request, "about.html",{"profile":prof , "summary" : summ, "school":schol, "skill":skills})



