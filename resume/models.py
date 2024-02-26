from django.db import models

# Create your models here.

class projects(models.Model):
    title = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    image =models.CharField(max_length=200, default='SOME STRING')
