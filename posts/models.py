from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    caption = models.TextField(max_length=250)
    post_image = models.ImageField(upload_to='react/', blank=True, default="default_post")

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} {self.caption}'
