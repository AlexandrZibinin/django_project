from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_category_from_cache


class ProductListView(ListView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (
                user.has_perm("catalog.set_publish_status")
                and user.has_perm("catalog.can_edit_description")
                and user.has_perm("catalog.can_edit_category")
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactsView(TemplateView):
    template_name = "catalog/contacts_view.html"


class CategoryListView(ListView, LoginRequiredMixin):
    model = Category
    success_url = reverse_lazy("catalog:home")

    def get_queryset(self):
        return get_category_from_cache()

