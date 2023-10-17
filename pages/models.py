from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.validators import FileExtensionValidator
from django.core.validators import URLValidator

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    last_name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    Phone_number = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    facebook_link = models.URLField(max_length=100, validators=[URLValidator()])
    twitter_link = models.URLField(max_length=100, validators=[URLValidator()])
    google_plus_link = models.URLField(max_length=100, validators=[URLValidator()])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
