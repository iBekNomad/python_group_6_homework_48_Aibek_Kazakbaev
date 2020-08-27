from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product
from .forms import ProductForm, SimpleSearchForm


class IndexView(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'product/index.html'
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['category', 'name']

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(amount__gt=0)
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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

    # def form_valid(self, form):
    #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
    #     issue = form.save(commit=False)
    #     issue.project = project
    #     issue.save()
    #     return redirect('project_view', pk=project.pk)


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
