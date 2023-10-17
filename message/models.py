from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sender_email = models.EmailField()
    product_name = models.CharField(max_length=255)
    customer_need = models.CharField(max_length=255, default='')  # Provide a default value
    city = models.CharField(max_length=100, default='')  # Provide a default value
    state = models.CharField(max_length=100, default='')  # Provide a default value
    phone = models.CharField(max_length=100, default='')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Using Django's ORM for database operations
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.product_name}"

# Create your models here.
