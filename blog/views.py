from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from pytils.translit import slugify

from blog.models import Blog


class BaseView(TemplateView):
    template_name = "blog/base_view.html"


class BlogListView(ListView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(public=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        "title",
        "text",
        "image",
        "public",
    )
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        "title",
        "text",
        "image",
        "public",
    )
    def get_success_url(self):
        return reverse_lazy('blog:blog_view', kwargs={'pk': self.object.pk})


    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
