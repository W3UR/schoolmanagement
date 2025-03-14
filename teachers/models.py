from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
    resume = models.FileField(upload_to='teacher_resumes/', blank=True, null=True)
    joining_letter = models.FileField(upload_to='teacher_letters/', blank=True, null=True)

    def __str__(self):
        return self.name
