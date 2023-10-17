from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['car_id', 'car_title', 'user_id', 'first_name', 'last_name', 'customer_need', 'city', 'state', 'message', 'email', 'phone']
