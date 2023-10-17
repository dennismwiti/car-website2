from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Contact
from .forms import ContactForm


def inquiry(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your request has been submitted, we will get back to you shortly.')

            # Redirect to the car details page using the correct parameter name (car_id)
            return redirect(reverse('car_details', args=[contact.car_id]))

    return render(request, 'accounts/dashboard.html')

