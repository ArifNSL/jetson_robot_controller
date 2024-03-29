# Generated by Django 3.2.16 on 2023-04-11 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_alter_userinfo_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='role',
            field=models.CharField(choices=[('robot', 'Robot'), ('user', 'User'), ('admin', 'Admin')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
