# Generated by Django 5.0.2 on 2024-03-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_alter_schools_school_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='Description',
            field=models.CharField(max_length=1000),
        ),
    ]
