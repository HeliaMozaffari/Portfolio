from django.contrib import admin
from .models import  project, profile,course, skill, experience, education, vlogCategory, vlogPost

admin.site.register(project)
admin.site.register(skill)
admin.site.register(experience)
admin.site.register(education)
admin.site.register(profile)
admin.site.register(course)
admin.site.register(vlogCategory)
admin.site.register(vlogPost)


# Register your models here.
