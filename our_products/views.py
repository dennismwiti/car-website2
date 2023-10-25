# import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Accessories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db import connection


# Create your views here.


def accessories_list(request):
				accessories = Accessories.objects.order_by('id').all()
				paginator = Paginator(accessories, 8)
				page = request.GET.get('page')
				paged_cars = paginator.get_page(page)

				featured_accessories = Accessories.objects.filter(is_featured=True).order_by('price').all()

				special_accessories = Accessories.objects.filter(is_special=True).order_by('price').all()

				context = {
								'accessories': accessories,
								'accessory': paged_cars,

								'featured_accessories': featured_accessories,

								'special_accessories': special_accessories,
				}

				return render(request, 'pages/our_products.html', context)


def accessory_detail(request, accessory_id):
				try:
								single_accessory = get_object_or_404(Accessories, pk=accessory_id)

				except Accessories.DoesNotExist:
								single_accessory = None

				context = {
								'single_accessory': single_accessory,

				}

				return render(request, 'products/accessory_details.html', context)


def filter_accessories(request):
				category = request.GET.get('category', '')
				selected_features = request.GET.getlist('features', [])
				min_price = request.GET.get('min_price')
				max_price = request.GET.get('max_price')
				type_slug = request.GET.get('type_slug', '')
				accessories = Accessories.objects.order_by('price').all()

				# Apply category filtering
				if category:
								accessories = accessories.filter(category=category)

				# Apply feature filtering
				if selected_features:
								accessories = accessories.filter(features__in=selected_features)

				# Apply price filtering
				if min_price:
								accessories = accessories.filter(price__gte=min_price)
				if max_price:
								accessories = accessories.filter(price__lte=max_price)

				# Apply type slug filtering
				if type_slug:
								accessories = accessories.filter(type_slug__iexact=type_slug)

				accessories = accessories.distinct()

				# Paginator settings
				page = request.GET.get('page', 1)
				items_per_page = 9  # Adjust as needed

				# Create a Paginator instance
				paginator = Paginator(accessories, items_per_page)

				try:
								# Get the current page
								accessories = paginator.page(page)
				except PageNotAnInteger:
								# If page is not an integer, deliver the first page.
								accessories = paginator.page(1)
				except EmptyPage:
								# If page is out of range (e.g., 9999), deliver the last page of results.
								accessories = paginator.page(paginator.num_pages)

				context = {
								'accessories': accessories,
								'selected_category': category,
								'selected_features': selected_features,
								'selected_type_slug': type_slug,
				}

				return render(request, 'products/filtered_accessories.html', context)


def accessory(request):
				all_accessory = Accessories.objects.order_by('price').all()
				paginator = Paginator(all_accessory, 6)
				page = request.GET.get('page')
				paged_accessory = paginator.get_page(page)

				data = {
								'all_accessory': all_accessory,
								'paged_accessory': paged_accessory,
				}

				return render(request, 'products/accessories.html', data)


# def search(request):
# 				query = request.GET.get('q', '')
#
# 				# Perform a case-insensitive search for accessory names
# 				results = Accessories.objects.filter(name__icontains=query)
#
# 				# Render the search results
# 				return render(request, 'filtered_accessories.html', {'results': results})


def quickview_detail(request, accessory_id):
				try:
								single_accessory = get_object_or_404(Accessories, pk=accessory_id)

								# Construct the full URL for the accessory_photo
								if single_accessory.accessory_photo:
												single_accessory.photo_url = settings.MEDIA_URL + single_accessory.accessory_photo.name
								else:
												single_accessory.photo_url = None

				except Accessories.DoesNotExist:
								single_accessory = None

				context = {
								'single_accessory': single_accessory,
				}

				return render(request, 'products/quick_view.html', context)


def send_email(request):
				if request.method == 'POST':
								# Assuming your form fields are named 'first_name', 'last_name', 'email', 'message'
								first_name = request.POST.get('first_name', '')
								last_name = request.POST.get('last_name', '')
								email = request.POST.get('email', '')
								message_text = request.POST.get('message', '')

								# # Construct the email subject and message
								# subject = f'New Inquiry from {first_name} {last_name}'
								# message = f'Name: {first_name} {last_name}\nEmail: {email}\n\nMessage:\n{message_text}'

								# # Send the email
								# send_mail(subject, message, email, ['blockbuster045@gmail.com'])

								# Get the admin user (assuming there's only one superuser)
								admin_user = User.objects.filter(is_superuser=True).first()

								if admin_user:
												admin_email = admin_user.email
												print(f"Admin Email: {admin_email}")

												# Set EMAIL_HOST_USER dynamically
												email_host_user = admin_email
												print(f"Email Host User: {email_host_user}")
												try:
																# Construct the email subject and message
																subject = f'New Inquiry from {first_name} {last_name}'
																message = f'Name: {first_name} {last_name}\nEmail: {email}\n\nMessage:\n{message_text}'

																# Send the email
																send_mail(subject, message, email_host_user, [admin_email])

																# Add a success message
																messages.success(request, 'Your message has been sent successfully!')
												except Exception as e:
																# Print any errors that occur during send_mail
																print(f"Error sending email: {e}")
																# Add an error message
																messages.error(request, 'There was an error sending your message.')
												else:
																# Add a message indicating no admin user found
																messages.error(request, 'No admin user found.')

												# Redirect to the same page
												return redirect(reverse('accessories'))
								else:
												# Handle GET requests if needed
												return redirect(reverse('filtered_accessories'))


def search_accessory(request):
				# Fetch the user's search query from the GET parameters
				search_query = request.GET.get('query', '')

				# Perform a basic search in your Accessory model
				results = Accessories.objects.filter(
								Q(name__icontains=search_query) |
								Q(type_slug__iexact=search_query) |
								Q(category__iexact=search_query)
				)

				# Print the SQL query
				if connection.queries:
								print(connection.queries[-1]['sql'])

				# If no search query, return all accessories
				if not search_query:
								results = Accessories.objects.all()

				# Pagination
				page = request.GET.get('page', 1)
				paginator = Paginator(results, 6)  # Show 10 results per page
				try:
								paged_accessory = paginator.page(page)
				except PageNotAnInteger:
								paged_accessory = paginator.page(1)
				except EmptyPage:
								paged_accessory = paginator.page(paginator.num_pages)

				context = {
								'results': results,
								'query': search_query,
								'paged_accessory': paged_accessory
				}
				return render(request, 'products/accessories.html', context)


# def get_random_nonce():
# 				return str(uuid.uuid4())
