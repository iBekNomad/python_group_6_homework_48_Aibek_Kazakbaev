from django import forms
from .models import CATEGORY_CHOICES, DEFAULT_CATEGORY

default_category = CATEGORY_CHOICES[0][0]


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=True, label='Описание')
    category = forms.ChoiceField(max_length=20, choices=default_category, initial=DEFAULT_CATEGORY,
                                 required=True, label='Категория')
    amount = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(min_value=0, required=True, label='Цена')
