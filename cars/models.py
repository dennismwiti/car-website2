import re
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):
    # state_choice = (
    #     ('AL', 'Alabama'),
    #     ('AK', 'Alaska'),
    #     ('AZ', 'Arizona'),
    #     ('AR', 'Arkansas'),
    #     ('CA', 'California'),
    #     ('CO', 'Colorado'),
    #     ('CT', 'Connecticut'),
    #     ('DE', 'Delaware'),
    #     ('DC', 'District Of Columbia'),
    #     ('FL', 'Florida'),
    #     ('GA', 'Georgia'),
    #     ('HI', 'Hawaii'),
    #     ('ID', 'Idaho'),
    #     ('IL', 'Illinois'),
    #     ('IN', 'Indiana'),
    #     ('IA', 'Iowa'),
    #     ('KE', 'Kenya'),
    #     ('KS', 'Kansas'),
    #     ('KY', 'Kentucky'),
    #     ('LA', 'Louisiana'),
    #     ('ME', 'Maine'),
    #     ('MD', 'Maryland'),
    #     ('MA', 'Massachusetts'),
    #     ('MI', 'Michigan'),
    #     ('MN', 'Minnesota'),
    #     ('MS', 'Mississippi'),
    #     ('MO', 'Missouri'),
    #     ('MT', 'Montana'),
    #     ('NE', 'Nebraska'),
    #     ('NV', 'Nevada'),
    #     ('NH', 'New Hampshire'),
    #     ('NJ', 'New Jersey'),
    #     ('NM', 'New Mexico'),
    #     ('NY', 'New York'),
    #     ('NC', 'North Carolina'),
    #     ('ND', 'North Dakota'),
    #     ('OH', 'Ohio'),
    #     ('OK', 'Oklahoma'),
    #     ('OR', 'Oregon'),
    #     ('PA', 'Pennsylvania'),
    #     ('RI', 'Rhode Island'),
    #     ('SC', 'South Carolina'),
    #     ('SD', 'South Dakota'),
    #     ('TN', 'Tennessee'),
    #     ('TX', 'Texas'),
    #     ('UT', 'Utah'),
    #     ('VT', 'Vermont'),
    #     ('VA', 'Virginia'),
    #     ('WA', 'Washington'),
    #     ('WV', 'West Virginia'),
    #     ('WI', 'Wisconsin'),
    #     ('WY', 'Wyoming'),
    # )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))
    #
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
    # state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(choices=city_choices, max_length=100)
    color = models.CharField(choices=color_choices, max_length=100)
    model = models.CharField(choices=models_choices, max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField(
        verbose_name='Price',
    )

    # include video_link
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
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    car_video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True,
                                 help_text="Upload a video of the car.")

    # def generate_video_thumbnail(self):
    #     if self.car_video:
    #         video_path = os.path.join(settings.MEDIA_ROOT, str(self.car_video))
    #         thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'thumbnails', f'thumbnail_{self.id}.jpg')
    #
    #         try:
    #             (
    #                 ffmpeg.input(video_path, ss=6)  # Extract thumbnail at 5 seconds into the video (adjust as needed)
    #                 .output(thumbnail_path, vf='select=gte(n\,0)', vframes=1, r=1, t=duration)
    #                 .run(overwrite_output=True)
    #             )
    #
    #             return f'media/thumbnails/thumbnail_{self.id}.jpg'
    #         except ffmpeg.Error as e:
    #             print(f'Error generating thumbnail: {e.stderr}')
    #
    #         return None

    features = MultiSelectField(choices=features_choices, max_length=255, blank=True)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    # passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100, unique=True)
    milage = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choices, max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
