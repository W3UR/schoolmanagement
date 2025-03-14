from django.db import models
from students.models import Student

class FeesGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    amount_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FeesType(models.Model):
    fee_group = models.ForeignKey(FeesGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Admission Fee / Apr25")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class FeesPayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Online', 'Online')])

    def __str__(self):
        return f"{self.student} - {self.amount} - {self.date}"
