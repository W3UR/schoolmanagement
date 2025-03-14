from django.db import models
from django.utils import timezone

class SchoolProfile(models.Model):
    school_name = models.CharField(max_length=255)
    principal_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=50, unique=True)
    logo = models.ImageField(upload_to='uploads/school_logos/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.school_name
