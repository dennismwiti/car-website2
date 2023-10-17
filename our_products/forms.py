from django import forms


class SortingForm(forms.Form):
    orderby = forms.ChoiceField(choices=[
        ('1', 'Sort by price: low to high'),
        ('2', 'Sort by price: high to low'),
        ('3', 'Product Name: Z'),
    ])
