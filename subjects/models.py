from django.db import models
from teachers.models import Teacher  # टीचर को जोड़ने के लिए

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    section = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} - {self.section}"

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SubjectAssignment(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('class_name', 'subject')

    def __str__(self):
        return f"{self.class_name} - {self.subject}"
