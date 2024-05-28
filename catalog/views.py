from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductCreateView(CreateView):
    model = Product
    fields = (
        "name",
        "description",
        "image",
        "category",
        "price",
        "created_at",
        "updated_at",
    )
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        "name",
        "description",
        "image",
        "category",
        "price",
        "created_at",
        "updated_at",
    )
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactsView(TemplateView):
    template_name = "catalog/contacts_view.html"
