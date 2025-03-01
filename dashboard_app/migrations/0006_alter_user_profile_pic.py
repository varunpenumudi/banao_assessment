# Generated by Django 5.0.2 on 2025-02-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0005_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_images/default.jpg', null=True, upload_to='profile_images'),
        ),
    ]
