# Generated by Django 5.0.2 on 2025-02-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0006_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('DOCTOR', 'doctor'), ('PATIENT', 'patient')], default='PATIENT', max_length=30),
        ),
    ]
