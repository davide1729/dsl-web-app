# Generated by Django 4.0.4 on 2022-05-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlboMacs', '0012_course_course_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(blank=True, default=None, to='AlboMacs.person'),
        ),
    ]
