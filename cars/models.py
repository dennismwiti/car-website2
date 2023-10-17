import re
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, validate_integer, validate_slug, validate_email
from django.core.exceptions import ValidationError


def validate_image_file_extension(value):
    if not value.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError('Only JPEG or PNG images are allowed.')


def validate_video_file_extension(value):
    if not value.name.lower().endswith(('.mp4', '.avi', '.mov')):
        raise ValidationError('Only MP4, AVI, or MOV videos are allowed.')


# def validate_integer_string(value):
#     try:
#         int(value)
#     except ValueError:
#         raise ValidationError('Enter a valid integer.')


# Create your models here.
class Car(models.Model):
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    brand_slug = (
        ('bmw', 'B.M.W'),
        ('toyota', 'TOYOTA'),
        ('volkswagen', 'VOLKSWAGEN'),
        ('morbius', 'MORBIUS'),
        ('honda', 'HONDA'),
        ('mazda', 'Mazda'),
        ('subaru', 'Subaru'),
        ('mercedes', 'Mercedes'),
        ('audi', 'Audi'),
        ('nissan', 'Nissan'),
        ('hyundai', 'Hyundai'),
        ('chevrolet', 'Chevrolet'),
        ('nissan', 'Nissan'),
        # Add more choices for other brands
    )

    door_choices = (
        ('2', '2'),
        ('4', '4'),
    )

    fuel_choices = (
        ('petroleum', 'PETROLEUM'),
        ('diesel', 'DIESEL'),
    )

    color_choices = (
        ('red', 'RED'),
        ('white', 'WHITE'),
        ('black', 'BLACK'),
        ('green', 'GREEN'),
        ('grey', 'GREY'),
        ('blue', 'BLUE'),
    )

    models_choices = (
        ('micro', 'Micro'),
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('sport car', 'Sport car'),
        ('suv', 'SUV'),
        ('pickup', 'Pickup'),
        ('van', 'Van'),
        ('lorry', 'Lorry'),
    )
    city_choices = (
        ('nairobi', 'Nairobi'),
        ('eldoret', 'Eldoret'),
        ('mombasa', 'Mombasa'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
    )

    car_title = models.CharField(max_length=255)
    brand_slug = models.SlugField(choices=brand_slug, max_length=200)
    city = models.CharField(choices=city_choices, max_length=100)
    color = models.CharField(choices=color_choices, max_length=100)
    model = models.CharField(choices=models_choices, max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField(
        verbose_name='Price',
        validators=[MinValueValidator(0)]
    )

    # # include video_link
    video_link = models.URLField(max_length=200, blank=True, null=True, help_text="Include your video link!")

    def save(self, *args, **kwargs):
        if self.video_link:
            # Extract video ID from YouTube or Vimeo links
            youtube_match = re.match(r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]+)', self.video_link)
            vimeo_match = re.match(r'(?:https?://)?(?:www\.)?vimeo\.com/(\d+)', self.video_link)

            if youtube_match:
                video_id = youtube_match.group(1)
                self.video_link = f'https://www.youtube.com/embed/{video_id}'
            elif vimeo_match:
                video_id = vimeo_match.group(1)
                self.video_link = f'https://player.vimeo.com/video/{video_id}'

        super().save(*args, **kwargs)

    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', validators=[validate_image_file_extension])
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])
    car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])
    car_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])
    car_photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/',
                                    blank=True, validators=[validate_image_file_extension])

    car_video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True,
                                 help_text="Upload a video of the car.", validators=[validate_video_file_extension])

    features = MultiSelectField(choices=features_choices, max_length=255, blank=True)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField(validators=[MinValueValidator(0)])
    doors = models.CharField(choices=door_choices, max_length=10)
    vin_no = models.CharField(max_length=100, unique=True)
    milage = models.IntegerField(validators=[MinValueValidator(0)])
    fuel_type = models.CharField(choices=fuel_choices, max_length=50)
    no_of_owners = models.CharField(max_length=100, validators=[validate_integer])
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title


# Custom validators
