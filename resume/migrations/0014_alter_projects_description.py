# Generated by Django 5.0.2 on 2024-03-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_projects_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Description',
            field=models.CharField(max_length=2000),
        ),
    ]
