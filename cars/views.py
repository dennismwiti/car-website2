from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.middleware.csrf import get_token
from django.views.decorators.cache import cache_page
# from django.views.decorators.http import require_POST
from .models import Car
import hashlib


# Create your views here.
def cars(request):
    all_cars = Car.objects.order_by('price')
    paginator = Paginator(all_cars, 9)
    page = request.GET.get('page', 1)

    try:
        paged_cars = paginator.page(page)
    except PageNotAnInteger:
        paged_cars = paginator.page(1)
    except EmptyPage:
        paged_cars = paginator.page(paginator.num_pages)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    brand_slug_search = Car.objects.values_list('brand_slug', flat=True).distinct()

    # Set CSRF token as HTTP Only cookie for security
    csrf_token = get_token(request)
    response = render(request, 'cars/cars.html', {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'brand_slug_search': brand_slug_search,
    })
    response.set_cookie('csrftoken', csrf_token, httponly=True, samesite='Strict')
    return response


def car_detail(request, id, no_car=False):
    try:
        single_car = get_object_or_404(Car, pk=id)
    except Car.DoesNotExist:
        single_car = None
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_details.html', data)


@cache_page(60 * 15)
def search(request):
    cars = Car.objects.order_by('price')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).order_by('year').distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    brand_slug_search = Car.objects.values_list('brand_slug', flat=True).distinct()

    # Refactor the search filters
    filters = {}
    for param in ['keyword', 'model', 'city', 'year', 'body_style', 'brand_slug', 'min_price', 'max_price']:
        value = request.GET.get(param)
        if value:
            # Handle min_price and max_price differently
            if param in ['min_price', 'max_price']:
                filters['price__' + ('gte' if param == 'min_price' else 'lte')] = value
            else:
                filters[f"{param}__icontains" if param == 'keyword' else f"{param}__iexact"] = value

    cars = cars.filter(**filters)

    response = render(request, 'cars/search.html', {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'brand_slug_search': brand_slug_search,
    })

    return response


def get_style_hash():
    style_content = "your_style_content_here"
    return hashlib.sha256(style_content.encode('utf-8')).hexdigest()


