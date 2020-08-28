from django.db.models import Q
from django.views.generic import ListView as DjangoListView

from webapp.forms import SimpleSearchForm


class SearchView(DjangoListView):
    search_form_class = SimpleSearchForm
    search_form_field = 'search'
    search_fields = []

    def get(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value(self.search_form)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['search_form'] = self.search_form
        context['search_value'] = self.search_value
        return context

    def get_queryset(self):
        data = super(SearchView, self).get_queryset()
        query = self.get_query(self.search_value)
        data = data.filter(query)
        return data

    def get_search_form(self):
        return self.search_form_class(data=self.request.GET)

    def get_search_value(self, form):
        search_value = None
        if form.is_valid():
            search_value = form.cleaned_data.get(self.search_form_field, None)
        return search_value

    def get_query(self, search_value):
        query = Q()
        if search_value:
            for field in self.search_fields:
                kwargs = {field: search_value}
                query = query | Q(**kwargs)
        return query
