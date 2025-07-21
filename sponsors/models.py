from django.db import models
from students.models import StudentModel
import re

class SponsorModel(models.Model):

    PHYSICAL = 'physical'
    LEGAL = 'legal'

    SPONSOR_TYPE_CHOICES = [
        (PHYSICAL, 'Физическое лицо'),
        (LEGAL, 'Юридическое лицо'),
    ]

    NEW = 'new'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'
    MODERATION = 'moderation'

    STATUS_CHOICES = [
        (NEW, 'Новый'),
        (CONFIRMED, 'Подтверждённый'),
        (CANCELED, 'Отменённый'),
        (MODERATION, 'В модернизации'),
    ]

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=9)
    sponsor_type = models.CharField(choices=SPONSOR_TYPE_CHOICES, default=PHYSICAL) 
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    sponsored_amount = models.DecimalField(max_digits=14, decimal_places=2)
    spend_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    status = models.CharField(choices=STATUS_CHOICES, default=NEW)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        if not self.phone_number.startswith('+998'):
            cleaned = re.sub(r'\D', '', self.phone_number)  # Удаляет пробелы, тире и т.п.
            if len(cleaned) == 9:
                self.phone_number = f'+998{cleaned}'
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'Sponsors'
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        ordering = ['created_at']

class SponsorToStudentModel(models.Model):
    sponsor = models.ForeignKey(SponsorModel, on_delete=models.CASCADE, related_name='sponsor_links')
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='student_links')
    allocated_amount = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sponsor.full_name} → {self.student.full_name}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.allocated_amount > (self.sponsor.sponsored_amount - self.sponsor.spend_amount):
                raise ValueError("Недостаточно средств у спонсора")
            if self.allocated_amount > (self.student.contract_amount - self.student.allocated_amount):
                raise ValueError("Сумма превышает контракт студента")

            self.sponsor.spend_amount += self.allocated_amount
            self.sponsor.save()

            self.student.allocated_amount += self.allocated_amount
            self.student.save()

            super().save(*args, **kwargs)

            super().save(*args, **kwargs)