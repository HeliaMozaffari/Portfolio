from django.db import models

# Create your models here.

class projects(models.Model):
    title = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    image =models.CharField(max_length=200, default='SOME STRING')
    image_link =models.CharField(max_length=200, default='SOME STRING')

class profile(models.Model):
    name = models.CharField(max_length=50)
    image =models.CharField(max_length=200, default='SOME STRING')
    summary =models.CharField(max_length=200)

class summary(models.Model):
    summary= models.CharField(max_length=200)

class schools(models.Model):
    school_name = models.CharField(max_length = 200)
    school_startyear= models.CharField(max_length= 4)
    school_endyear= models.CharField(max_length= 4)

class courses(models.Model):
    course_name = models.CharField(max_length = 200)
    course_description = models.CharField(max_length = 200)
    course_school = models.CharField(max_length = 200)

class companies(models.Model):
    company_name =  models.CharField(max_length = 200)
    company_startyear = models.CharField(max_length = 4)
    company_endyear = models.CharField(max_length = 4)
    Description = models.CharField(max_length = 200)

class skills(models.Model):
     skills =  models.CharField(max_length = 200)







