from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Message
from django.contrib.auth.decorators import login_required


@login_required
def send_message(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            customer_need = request.POST['customer_need']
            product_name = request.POST['product_name']
            city = request.POST['city']
            state = request.POST['state']
            email = request.POST['email']
            phone = request.POST['phone']
            user_message_text = request.POST['message']

            # Set sender based on authentication status
            sender_user = request.user if request.user.is_authenticated else None

            # Create and save the Message model instance
            user_message = Message(
                first_name=first_name,
                last_name=last_name,
                sender_email=email,  # Use the provided email directly
                product_name=product_name,
                customer_need=customer_need,
                city=city,
                state=state,
                phone=phone,
                message=user_message_text
            )
            user_message.save()

            # Add a success message
            messages.success(request, 'Your message has been saved successfully!')

            # Redirect to the same page or another page
            return redirect(reverse('accessories'))
        except Exception as e:
            # Print any errors that occur during message creation
            print(f"Error saving message: {e}")
            # Add an error message
            messages.error(request, 'There was an error saving your message.')

    # Handle GET requests if needed
    return redirect(reverse('filter_accessories'))
