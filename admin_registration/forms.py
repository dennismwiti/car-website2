# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
from .models import AdminUser
# from django.utils.text import slugify
# import uuid


class AdminRegistrationForm(UserCreationForm):
				fullname = forms.CharField(max_length=255, label='Full Name')
				email = forms.EmailField(label='Email')
				# username = forms.CharField(max_length=150, label='Username')

				class Meta:
								model = AdminUser
								fields = ['fullname', 'email', 'password1', 'password2']

				def save(self, commit=True):
								user = super().save(commit=False)
								user.email = self.cleaned_data["email"]
								user.fullname = self.cleaned_data["fullname"]
								# user.username = self.cleaned_data["username"]

								# Generate a unique username based on the email or use a different logic
								# user.username = slugify(user.email.split('@')[0]) + str(uuid.uuid4())[:8]

								# Set is staff and superuser to true for every admin registered
								user.is_staff = True
								user.is_superuser = True

								if commit:
												user.save()

								# Debugging statements
								print(f"User saved: {user}")

								return user
