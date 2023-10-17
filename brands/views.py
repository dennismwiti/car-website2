from django.shortcuts import render
from cars.models import Car
# Create your views here.


def brand_cars(request, brand_slug):
    brand_cars = Car.objects.filter(brand_slug=brand_slug)

    # for car in brand_cars:
    #     formatted_miles = "{:,}".format(car.miles)
    #     car.formatted_miles = formatted_miles

    context = {
        'cars': brand_cars,
        'brand_slug': brand_slug
    }
    return render(request, 'brand_cars.html', context)

# def toyota_cars(request):
#     toyota_cars = Car.objects.filter(brand='Toyota')
#     return render(request, 'toyota_cars.html', {'cars': toyota_cars})
#
#
# def bmw_cars(request):
#     bmw_cars = Car.objects.filter(brand='BMW')
#     return render(request, 'bmw_cars.html', {'cars': bmw_cars})
#
#
# def volkswagen_cars(request):
#     volkswagen_cars = Car.objects.filter(brand='VOLKSWAGEN')
#     return render(request, 'volkswagen_cars.html', {'cars': volkswagen_cars})
