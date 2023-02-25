from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    """
    Follow model
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account_following')
    created_date = models.DateTimeField(auto_now_add=True)
    account_followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account_followed')

    class Meta:
        ordering = ['-created_date']
        unique_together = ['owner', 'account_followed']

    def __str__(self):
        return f"{self.owner} {self.account_followed}"
