from django.db import models
from django.core.validators import RegexValidator
from subjects.models import Class  # Subjects ऐप से क्लास मॉडल इम्पोर्ट करें

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Christian', 'Christian'),
        ('Sikh', 'Sikh'),
        ('Other', 'Other'),
    ]

    CASTE_CHOICES = [
        ('General', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    admission_number = models.CharField(max_length=20, unique=True, verbose_name="Admission Number")
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    father_name = models.CharField(max_length=100, verbose_name="Father's Name")
    mother_name = models.CharField(max_length=100, verbose_name="Mother's Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    date_of_admission = models.DateField(verbose_name="Date of Admission")
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Class")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Gender")
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, verbose_name="Religion")
    caste_category = models.CharField(max_length=20, choices=CASTE_CHOICES, verbose_name="Caste Category")
    address = models.TextField(verbose_name="Address")
    mobile_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^[0-9]{10}$', message="Mobile number must be 10 digits.")],
        verbose_name="Mobile Number"
    )
    email = models.EmailField(verbose_name="Email")
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, verbose_name="Blood Group")
    student_image = models.ImageField(upload_to='students/images/', verbose_name="Student Image")
    aadhar_card = models.FileField(upload_to='students/documents/', verbose_name="Aadhar Card")
    transfer_certificate = models.FileField(upload_to='students/documents/', verbose_name="Transfer Certificate")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"

def get_default_student():
    """पहला स्टूडेंट ढूंढकर डिफ़ॉल्ट सेट करता है, अगर कोई स्टूडेंट नहीं है तो None लौटाता है।"""
    student = Student.objects.first()
    return student.id if student else None


class StudentEnrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,  # पहले इसे nullable रखें
        blank=True,
        default=get_default_student  # पहला स्टूडेंट डिफ़ॉल्ट में सेट करें
    )
    enrollment_date = models.DateField()
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.class_name}"
