from django.db import models
from students.models import Student  # Import Student Model

class Route(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Route Name")

    def __str__(self):
        return self.name

class Stoppage(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="Route")
    name = models.CharField(max_length=100, unique=True, verbose_name="Stoppage Name")

    class Meta:
        unique_together = ('route', 'name')  # Ensure unique stoppages per route

    def __str__(self):
        return f"{self.route.name} - {self.name}"

class TransportAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student")
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="Route")
    stoppage = models.ForeignKey(Stoppage, on_delete=models.CASCADE, verbose_name="Stoppage")

    class Meta:
        unique_together = ('student', 'route', 'stoppage')  # Ensure unique assignments

    def __str__(self):
        return f"{self.student.first_name} - {self.route.name} - {self.stoppage.name}"
