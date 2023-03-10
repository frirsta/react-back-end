from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class BusinessProfile(models.Model):
    """
    Buisness Profile model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=300)
    business_description = models.TextField(max_length=500)
    phone_number = PhoneNumberField()
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    business_image = models.ImageField(
        upload_to='react/', default='default_business_profile')

    class Meta:
        ordering = ['-registration_date']

    def __str__(self):
        return f"{self.business_name}'s business profile"
