from django import forms
from django.core.exceptions import ValidationError

from .models import CATEGORY_CHOICES, Product

default_category = CATEGORY_CHOICES[0][0]


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=forms.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, initial=default_category, required=True, label='Категория')
    amount = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(min_value=0, required=True, label='Цена')

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
