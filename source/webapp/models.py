from django.db import models
from django.core.validators import MinValueValidator


DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = [
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Еда'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Интсрументы'),
    ('toys', 'Игрушки')
]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=20, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES,
                                verbose_name='Категория')
    amount = models.IntegerField(verbose_name='Остаток', validators=(MinValueValidator(0),))
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2,
                                validators=(MinValueValidator(0),))

    def __str__(self):
        return f'{self.name} - {self.amount}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='carts', on_delete=models.CASCADE, verbose_name='Продукты')
    amount = models.IntegerField(verbose_name='Остаток в корзине')

    def __str__(self):
        return f'{self.product} - {self.amount}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
