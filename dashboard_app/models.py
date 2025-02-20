from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("DOCTOR", "doctor"),
        ("PATIENT", "patient")
    )
    profile_pic = models.ImageField(null=True, blank=True, default='/profile_images/default.jpg',  upload_to='profile_images')
    role = models.CharField(max_length=30, default='PATIENT', choices=ROLE_CHOICES, null=False)
    address = models.CharField(max_length=300, null=True)