# Generated by Django 4.0.4 on 2022-05-23 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlboMacs', '0003_remove_news_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ssd', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=10)),
                ('cfu', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
