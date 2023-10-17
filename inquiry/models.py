from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator
from datetime import datetime


class Inquiry(models.Model):
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=300)
    user_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=200, validators=[MaxLengthValidator(200)])
    last_name = models.CharField(max_length=200, validators=[MaxLengthValidator(200)])
    customer_need = models.CharField(max_length=300, validators=[MaxLengthValidator(300)])
    city = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    state = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    message = models.TextField(blank=True, validators=[MaxLengthValidator(1000)])  # Adjust max length as needed
    email = models.EmailField(max_length=200, validators=[EmailValidator(), MaxLengthValidator(200)])
    phone = models.CharField(max_length=20, blank=True, validators=[MaxLengthValidator(20)])
    create_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email
