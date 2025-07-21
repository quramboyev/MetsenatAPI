from django.db import models
import re

class StudentModel(models.Model):
    
    BACHELOR = 'bachelor'
    MASTER = 'master'

    STUDENT_TYPE_CHOICES = [
        (BACHELOR, 'Бакалавриат'),
        (MASTER, 'Магистратура'),
    ]

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=9)
    student_type = models.CharField(max_length=20, choices=STUDENT_TYPE_CHOICES, default=BACHELOR)
    university = models.ForeignKey('UniversityModel', on_delete=models.CASCADE, related_name='students')
    contract_amount = models.DecimalField(max_digits=14, decimal_places=2)
    allocated_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.phone_number.startswith('+998'):
            cleaned = re.sub(r'\D', '', self.phone_number)  # Удаляет пробелы, тире и т.п.
            if len(cleaned) == 9:
                self.phone_number = f'+998{cleaned}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class UniversityModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name