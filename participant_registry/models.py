from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Participant(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    reference_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

   
    def __str__(self):
        return self.name

    def generate_reference_number(self):
        return f"{self.name}-{self.id}" 