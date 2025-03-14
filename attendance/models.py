from django.db import models


class Attendance(models.Model):
    date = models.DateField()
    present = models.IntegerField()
    absent = models.IntegerField()

    def __str__(self):
        return f"{self.date} - हाज़िर: {self.present}, अनुपस्थित: {self.absent}"
