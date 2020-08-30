from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, DeleteView, ListView, DetailView

from webapp.forms import OrderForm
from webapp.models import Product, Cart, Order, CheckOutOrder
from django.shortcuts import redirect, get_object_or_404

from webapp.views import SearchView


class OrderCreateView(CreateView):
    template_name = 'cart/cart_index.html'
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        if form.is_valid():
            order = Order.objects.create(user_name=form.cleaned_data['user_name'],
                                         phone_number=form.cleaned_data['phone_number'],
                                         address=form.cleaned_data['address'])

            for item in Cart.objects.all():
                CheckOutOrder.objects.create(checkout_product_id=item.product.pk, order_id=order.pk,
                                             total_amount=item.amount)

        Cart.objects.all().delete()
        return redirect('order_index')


class OrderIndexView(SearchView):
    model = CheckOutOrder
    template_name = 'order/order_index.html'
    paginate_by = 5
    context_object_name = 'checks'
