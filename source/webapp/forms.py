from django import forms
from django.core.exceptions import ValidationError

from .models import CATEGORY_CHOICES, Product, Cart, Order

default_category = CATEGORY_CHOICES[0][0]


class ProductForm(forms.ModelForm):
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=forms.Textarea)

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'amount', 'price']

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        amount = cleaned_data.get('amount')

        if amount < 1:
            errors.append(ValidationError('Amount of product must be more than 0!'))
        if errors:
            raise ValidationError(errors)
        return cleaned_data


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['user_name', 'phone_number', 'address']
