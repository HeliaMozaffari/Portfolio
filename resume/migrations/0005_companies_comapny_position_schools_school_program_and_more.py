# Generated by Django 5.0.2 on 2024-02-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_companies_courses_profile_schools_skills_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='comapny_position',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='schools',
            name='school_program',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='summary',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]