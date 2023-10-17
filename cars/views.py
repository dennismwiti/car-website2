from django.shortcuts import render, get_object_or_404
from .models import Car
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(request):
    all_cars = Car.objects.order_by('price')
    paginator = Paginator(all_cars, 9)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    brand_slug_search = Car.objects.values_list('brand_slug', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'brand_slug_search': brand_slug_search,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id, no_car=False):
    try:
        single_car = get_object_or_404(Car, pk=id)
    except Car.DoesNotExist:
        single_car = None
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_details.html', data)


def search(request):
    cars = Car.objects.order_by('price')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).order_by('year').distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    brand_slug_search = Car.objects.values_list('brand_slug', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'brand_slug' in request.GET:
        brand_slug = request.GET['brand_slug']
        if brand_slug:
            cars = cars.filter(brand_slug__iexact=brand_slug)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        if min_price:
            cars = cars.filter(price__gte=min_price)

    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'brand_slug_search': brand_slug_search,
    }
    return render(request, 'cars/search.html', data)



