import re
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, validate_image_file_extension


# Create an Accessories model with a ForeignKey to Category
class Accessories(models.Model):
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    category_choice = (
        ('Interior Accessories', 'Interior Accessories'),
        ('Exterior Accessories', 'Exterior Accessories'),
        ('Perfomance Accessories', 'Perfomance Accessories'),
        ('Safety and Security Accessories', 'Safety and Security Accessories'),
        ('Electronics and Entertainment', 'Electronics and Entertainment'),
        ('Lighting Accessories', 'Lighting Accessories'),
        ('Utility Accessories', 'Utility Accessories'),
        ('Appearance Accessories', 'Appearance Accessories'),
    )

    Type_slug = (
        ('Floor Mats', 'Floor-Mats'),
        ('liners', 'liners'),
        ('Seat Covers', 'Seat-Covers'),
        ('Seat cushions', 'Seat-Cushions'),
        ('Steering Wheel Covers', 'Steering-Wheel-Covers'),
        ('Sunshades', 'Sunshades'),
        ('Dash Covers', 'Dash-Covers'),
        ('Car Covers', 'Car-Covers'),
        ('Roof Racks', 'Roof-Racks'),
        ('Bike Racks', 'Bike-Racks'),
        ('Running Boards', 'Running-Boards'),
        ('Fender Flares', 'Fender-Flares'),
        ('Air Filters', 'Air-Filters'),
        ('Exhaust Systems', 'Exhaust-Systems'),
        ('Tuning Chips', 'Tuning-Chips'),
        ('Suspension Upgrades', 'Suspension-Upgrades'),
        ('Performance Brakes', 'Performance-Brakes'),
        ('Car Stereos', 'Car-Stereos'),
        ('Backup Cameras', 'Backup-Cameras'),
        ('Bluetooth Kits', 'Bluetooth-Kits'),
        ('Dash Cams', 'Dash-Cams'),
        ('Alarm Systems', 'Alarm-Systems'),
        ('Car Safety Kits', 'Car-Safety-Kits'),
        ('Parking Sensors', 'Parking-Sensors'),
        ('Blind Spot Mirrors', 'Blind-Spot-Mirrors'),
        ('Locking Wheel Nuts', 'Locking-Wheel-Nuts'),
        ('LED Headlights', 'LED-Headlights'),
        ('Fog Lights', 'Fog-Lights'),
        ('Interior LED Lights', 'Interior-LED-Lights'),
        ('Underglow Lights', 'Underglow-Lights'),
        ('Light Bars', 'Light-Bars'),
        ('Cargo Organizers', 'Cargo-Organizers'),
        ('Car Hitches', 'Car-Hitches'),
        ('Tire Inflators', 'Tire-Inflators'),
        ('Car Tents', 'Car-Tents'),
        ('Tool Kits', 'Tool-Kits'),
        ('Chrome Trim', 'Chrome-Trim'),
        ('Window Tinting', 'Window-Tinting'),
        ('Body Kits', 'Body-Kits'),
        ('Grille Guards', 'Grille-Guards'),
        ('Vinyl Decals', 'Vinyl-Decals'),
        ('Car covers', 'Car-covers'),
    )

    color_choices = (
        ('red', 'RED'),
        ('white', 'WHITE'),
        ('black', 'BLACK'),
        ('green', 'GREEN'),
        ('gray', 'GRAY'),
        ('blue', 'BLUE'),
        ('beige', 'BEIGE'),
        ('blue', 'BROWN'),
        ('yellow', 'YELLOW'),
        ('orange', 'ORANGE'),
        ('silver', 'SILVER'),
        ('carbon fiber', 'CARBON FIBER'),
    )

    feature_choices = (
        ('Adjustability', 'Adjustability'),
        ('Heating and Cooling', 'Heating and Cooling'),
        ('Smart Technology', 'Smart Technology'),
        ('Wireless Charging', 'Wireless Charging'),
        ('Waterproof and Weatherproof', 'Waterproof and Weatherproof'),
        ('LED Lighting', 'LED Lighting'),
        ('Noise Reduction', 'Noise Reduction'),
        ('Remote Control', 'Remote Control'),
        ('Safety Features', 'Safety Features'),
        ('Durability', 'Durability'),
        ('Easy Installation', 'Easy Installation'),
        ('Customization', 'Customization'),
        ('Quick Release', 'Quick Release'),
        ('Safety Reflectors', 'Safety Reflectors'),
        ('Anti-Theft Measures', 'Anti-Theft Measures'),
        ('UV Protection', 'UV Protection'),
        ('Ventilation', 'Ventilation'),
        ('Stain Resistance', 'Stain Resistance'),
        ('Compatibility', 'Compatibility'),
        ('Multi-Functionality', 'Multi-Functionality'),
    )

    name = models.CharField(max_length=500, verbose_name='Accessory Name')
    color = models.CharField(choices=color_choices, verbose_name='Color', max_length=255)
    category = models.CharField(choices=category_choice, max_length=500)
    type_slug = models.SlugField(choices=[(slugify(choice[0]), choice[1]) for choice in Type_slug], max_length=500)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    accessory_photo = models.ImageField(upload_to='accessories/%Y/%m/%d/', verbose_name='Image', blank=True, null=True,
                                        validators=[validate_image_file_extension])
    features = MultiSelectField(choices=feature_choices, verbose_name='Features', blank=True, max_length=300)
    is_featured = models.BooleanField(default=False, verbose_name='Is Featured')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    is_special = models.BooleanField(default=False, verbose_name='Is Special')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
