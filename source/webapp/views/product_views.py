from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .base_views import SearchView

from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(SearchView):
    model = Product
    template_name = 'product/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 5
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = reverse_lazy('index')
