# Generated by Django 5.0.2 on 2024-02-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_companies_comapny_position_schools_school_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(default='SOME STRING', max_length=200)),
                ('skill_description', models.CharField(default='SOME STRING', max_length=200)),
                ('skill_course', models.CharField(default='SOME STRING', max_length=200)),
                ('skill_position', models.CharField(default='SOME STRING', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='skills',
        ),
    ]