from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView

from webapp.models import Product, Cart
from django.shortcuts import redirect, get_object_or_404


from webapp.views import SearchView


class CartView(SearchView):
    template_name = 'cart/cart_index.html'
    model = Cart
    ordering = ['amount', 'product']
    search_fields = ['product__icontains']
    paginate_by = 5
    context_object_name = 'carts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CartAddView(CreateView):
    model = Cart

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        try:
            product.amount -= 1
            cart = Cart.objects.get(product=product)
            cart.amount += 1
            cart.save()
        except ObjectDoesNotExist:
            if product.amount == 0:
                return redirect('index')
            else:
                Cart.objects.create(product=product, amount=1)
        product.save()
        return redirect('index')


class CartDeleteView(DeleteView):
    model = Cart

    def get(self, request, *args, **kwargs):
        return self.delete(request, Product, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('cart_index')
