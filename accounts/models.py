from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, )
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bio = models.TextField(max_length=500)
    profile_image = models.ImageField(upload_to='react/',
                                                default='default_profile')

    class Meta:
        ordering = ['-registration_date']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
