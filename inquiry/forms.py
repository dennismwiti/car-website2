from django import forms


class InquiryForm(forms.Form):
    car_id = forms.IntegerField()
    car_title = forms.CharField(max_length=300)
    user_id = forms.IntegerField(required=False)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    customer_need = forms.CharField(max_length=300)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    phone = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=False)
