from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Contact model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=100, blank=False)
    content = models.TextField(max_length=500, blank=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.owner} {self.title}'
