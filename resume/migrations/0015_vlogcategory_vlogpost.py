# Generated by Django 5.0.2 on 2024-03-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_alter_projects_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='vlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlogCategory_title', models.CharField(default='SOME STRING', max_length=200)),
                ('vlogCategory_pic', models.CharField(default='SOME STRING', max_length=500)),
                ('vlogCategory_Description', models.CharField(default='SOME STRING', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='vlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlogPost_title', models.CharField(default='SOME STRING', max_length=200)),
                ('vlogPost_iframe', models.CharField(default='SOME STRING', max_length=600)),
            ],
        ),
    ]
