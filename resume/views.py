from django.shortcuts import render, HttpResponse
from .models import  project, profile, education, course, skill, experience, vlogCategory, vlogPost

# Create your views here.

def portfolio(request):
    proj = project.objects.all()
    return render(request, "portfolio.html",{ "project" : proj})


def about(request):
    prof = profile.objects.all()
    edu = education.objects.all()
    cou = course.objects.all()
    skil = skill.objects.all()
    exper = experience.objects.all()
    return render(request, "about.html",{"education": edu, "profile":prof, "course": cou, "skill":skil, "experience":exper})


def Vlog(request):
    vlogC = vlogCategory.objects.all()
    vlogP = vlogPost.objects.all()
    return render(request, "Vlog.html",{"vlogPost":vlogP , "vlogCategory" : vlogC})
