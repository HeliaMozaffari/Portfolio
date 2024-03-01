from django.db import models

# Create your models here.

class projects(models.Model):
    title = models.CharField(max_length=50)
    Description = models.CharField(max_length=2000)
    image =models.CharField(max_length=200, default='SOME STRING')
    image_link =models.CharField(max_length=200, default='SOME STRING')

class profile(models.Model):
    name = models.CharField(max_length=50 , default='SOME STRING')
    image =models.CharField(max_length=200, default='SOME STRING')
    summary =models.CharField(max_length=200 , default='SOME STRING')

class summary(models.Model):
    summary= models.CharField(max_length=2000)

class schools(models.Model):
    school_name = models.CharField(max_length = 200)
    school_description = models.CharField(max_length = 1000 , default='SOME STRING')
    school_program = models.CharField(max_length = 200  , default='SOME STRING')
    school_startyear= models.CharField(max_length= 4)
    school_endyear= models.CharField(max_length= 4)

class courses(models.Model):
    course_name = models.CharField(max_length = 200)
    course_description = models.CharField(max_length = 200)
    course_school = models.CharField(max_length = 200)

class companies(models.Model):
    company_name =  models.CharField(max_length = 200)
    comapny_position = models.CharField(max_length = 200  , default='SOME STRING')
    company_startyear = models.CharField(max_length = 4)
    company_endyear = models.CharField(max_length = 4)
    Description = models.CharField(max_length = 1000)

class skill(models.Model):
    skill =  models.CharField(max_length = 200  , default='SOME STRING')
    skill_description =  models.CharField(max_length = 200  , default='SOME STRING')
    skill_course =  models.CharField(max_length = 200  , default='SOME STRING')
    skill_position =  models.CharField(max_length = 200  , default='SOME STRING')







