from django import forms
from .models import Product


choices = (
        ('ascending', 'A-Z'),
        ('Hr', 'Highest Rating'),
    )
class Sort(forms.Form):
        model = Product
        sort = forms.Select(choices=choices)