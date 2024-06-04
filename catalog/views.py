from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactsView(TemplateView):
    template_name = "catalog/contacts_view.html"
