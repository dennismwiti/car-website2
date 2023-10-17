from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True,
                                       default=datetime.now)

    def save(self, *args, **kwargs):
        # Using Django's ORM to prevent SQL injection
        Contact.objects.raw(
            """
            INSERT INTO contacts_contact (first_name, last_name, car_id, customer_need, car_title, city, state, email, 
            phone, message, user_id, create_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            [self.first_name, self.last_name, self.car_id, self.customer_need, self.car_title,
             self.city, self.state, self.email, self.phone, self.message, self.user_id, self.create_date]
        )

    def __str__(self):
        return self.email
