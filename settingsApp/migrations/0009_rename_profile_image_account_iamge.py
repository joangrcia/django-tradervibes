# Generated by Django 4.2.4 on 2023-08-29 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qn_settings', '0008_alter_account_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='profile_image',
            new_name='iamge',
        ),
    ]
