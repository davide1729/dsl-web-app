# Generated by Django 4.0.4 on 2022-05-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlboMacs', '0019_delete_achievement2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='person',
            field=models.ManyToManyField(blank=True, default=None, to='AlboMacs.person'),
        ),
    ]
