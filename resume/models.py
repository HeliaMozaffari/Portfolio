from django.db import models
import datetime

# Create your models here.
class project(models.Model):
    project_ID = models.CharField(max_length=20, default='Not Stated')
    project_name = models.CharField(max_length=50, default='Not Stated')
    project_date = models.DateField(default=datetime.date.today)
    project_link = models.CharField(max_length=500, default='Not Stated')
    project_picture = models.CharField(max_length=500, default='Not Stated')
    project_description = models.CharField(max_length=2000, default='Not Stated')

class profile(models.Model):
    profile_ID = models.CharField(max_length=4, default='Not Stated')
    profile_name = models.CharField(max_length=50, default='Not Stated')
    profile_email = models.CharField(max_length=50, default='Not Stated')
    profile_phone = models.CharField(max_length=20, default='Not Stated')
    profile_city = models.CharField(max_length=20, default='Not Stated')
    profile_province = models.CharField(max_length=2, default='Not Stated')
    profile_picture = models.CharField(max_length=500, default='Not Stated')
    profile_status = models.CharField(max_length=1, default='0')
    profile_bio = models.CharField(max_length=4000, default='Not Stated')
    profile_summary = models.CharField(max_length=4000, default='Not Stated')

class education(models.Model):
    education_ID = models.CharField(max_length=4, default='Not Stated')
    profile_ID = models.CharField(max_length=4, default='Not Stated')
    education_schoolname = models.CharField(max_length=50, default='Not Stated')
    education_schoolprogram = models.CharField(max_length=50, default='Not Stated')
    education_schoolcity = models.CharField(max_length=50, default='Not Stated')
    education_schoolprovince = models.CharField(max_length=2, default='Not Stated')
    education_programstart = models.DateField(default=datetime.date.today)
    education_programend = models.DateField(default=datetime.date.today)
    education_programdescription =  models.CharField(max_length=2000, default='Not Stated')

class course(models.Model):
    course_ID = models.CharField(max_length=4, default='Not Stated')
    education_ID = models.CharField(max_length=4, default='Not Stated')
    course_name = models.CharField(max_length=4, default='Not Stated')
    course_description = models.CharField(max_length=4000, default='Not Stated')

class skill(models.Model):
    skill_ID = models.CharField(max_length=4, default='Not Stated')
    project_ID = models.CharField(max_length=4, default='Not Stated')
    course_ID = models.CharField(max_length=4, default='Not Stated')
    skill_name = models.CharField(max_length=50, default='Not Stated')
    skill_desccription = models.CharField(max_length=2000, default='Not Stated')

class experience(models.Model):
    experience_ID =  models.CharField(max_length=4, default='Not Stated')
    profile_ID =  models.CharField(max_length=4, default='Not Stated')
    experience_name =  models.CharField(max_length=50, default='Not Stated')
    experience_position =  models.CharField(max_length=50, default='Not Stated')
    experience_city =  models.CharField(max_length=50, default='Not Stated')
    experience_province =  models.CharField(max_length=2, default='Not Stated')
    experience_start =  models.DateField(default=datetime.date.today)
    experience_end = models.DateField(default=datetime.date.today)
    experience_description = models.CharField(max_length=4000, default='Not Stated')

class vlogCategory(models.Model):
    vlogCategory_title = models.CharField(max_length = 200  , default='SOME STRING')
    vlogCategory_pic = models.CharField(max_length = 500  , default='SOME STRING')
    vlogCategory_Description = models.CharField(max_length = 1000  , default='SOME STRING') 

class vlogPost(models.Model):
    vlogPost_title =  models.CharField(max_length = 200  , default='SOME STRING')
    vlogPost_description =  models.CharField(max_length = 1000  , default='SOME STRING')
    vlogPost_iframe = models.CharField(max_length = 600  , default='SOME STRING')



