from django.db import models
from datetime import datetime
# Create your models here.


class Inquiry(models.Model):
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=300)
    user_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    customer_need = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
