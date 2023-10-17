from django.shortcuts import render, redirect
from .forms import InquiryForm
from .models import Inquiry
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.models import User


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = Inquiry.objects.create(**form.cleaned_data)

            # Send email notification to admin
            subject = 'You Have A New Inquiry'
            message = f'You have a new inquiry from your Website:\n\n{form.cleaned_data["message"]}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_FROM_EMAIL]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            messages.success(request, 'Inquiry submitted successfully.')
            return redirect('dashboard')
    else:
        form = InquiryForm()

    return render(request, 'cars/cars.html', {'form': form})


def dashboard(request):
    inquiries = Inquiry.objects.all()  # Retrieve all inquiries from the database

    data = {
        'inquiries': inquiries,
    }
    return render(request, 'accounts/dashboard.html', data)


def delete_inquiry(request, inquiry_id):
    try:
        inquiry = Inquiry.objects.get(pk=inquiry_id)

        inquiry.delete()

        messages.success(request, 'Inquiry has been deleted successfully.')
    except Inquiry.DoesNotExist:

        messages.error(request, 'Inquiry deos not exist.')

    return redirect('dashboard')

