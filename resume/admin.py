from django.contrib import admin
from .models import projects, profile, summary, schools, courses, companies, skill

admin.site.register(projects)
admin.site.register(profile)
admin.site.register(summary)
admin.site.register(schools)
admin.site.register(courses)
admin.site.register(companies)
admin.site.register(skill)

# Register your models here.
