# Generated by Django 4.2.4 on 2023-09-12 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('copytrade', '0006_alter_mastercopytrade_harga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metatraders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('ip_address', models.CharField(blank=True, max_length=50)),
                ('port', models.CharField(blank=True, max_length=10)),
                ('token', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mastercopytrade',
            name='user',
        ),
        migrations.DeleteModel(
            name='FollowerCopyTrade',
        ),
        migrations.DeleteModel(
            name='MasterCopyTrade',
        ),
    ]
