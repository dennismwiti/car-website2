from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['car_id', 'car_title', 'user_id', 'first_name', 'last_name', 'customer_need',
                  'city', 'state', 'email', 'phone', 'message']
