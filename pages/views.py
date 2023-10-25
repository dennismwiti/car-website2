from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
# import uuid
import hashlib

# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('price')
    all_cars = Car.objects.order_by('price')
    model_search = Car.objects.values_list('model', flat=True).order_by('model').distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).order_by('year').distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    brand_slug_search = Car.objects.values_list('brand_slug', flat=True).order_by('brand_slug').distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'brand_slug_search': brand_slug_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new messages from CarDealer Website regarding ' + subject
        message_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email

        # try:
        #     send_mail(
        #         email_subject,
        #         message_body,
        #         'blockbuster045@gmail.com',
        #         [admin_email],
        #         fail_silently=False,
        #     )
        #     messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        #     return redirect('contact')
        # except Exception as e:
        #     print(f"Email sending error: {str(e)}")
        from_email = email  # Use the user's email as the sender
        recipient_list = ['blockbuster045@gmail.com']  # Replace with the admin's Gmail address

        send_mail(
            email_subject,
            message_body,
            from_email,
            recipient_list,
            fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')

    return render(request, 'pages/contact.html')


# def get_random_nonce():
#     return str(uuid.uuid4())

def get_style_hash():
    style_content = "your_style_content_here"
    return hashlib.sha256(style_content.encode('utf-8')).hexdigest()
