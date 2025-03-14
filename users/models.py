from django.contrib.auth.models import AbstractUser
from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    mobile = models.CharField(max_length=15, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    allowed_modules = models.ManyToManyField(Module, blank=True)  # ✅ एक्सेस कंट्रोल

    def __str__(self):
        return f"{self.username} - {self.role}"
