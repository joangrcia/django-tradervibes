# Generated by Django 4.2.4 on 2023-09-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articelApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
