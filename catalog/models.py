from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="catalog/photo", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        related_name="categories",
    )
    price = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    owner = models.ForeignKey(
        User, verbose_name="Создатель", blank=True, null=True, on_delete=models.SET_NULL
    )
    is_publish = models.BooleanField(
        null=False, default=False, verbose_name="Признак публикации"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("set_publish_status", "Can publish"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_category", "Can edit category"),
        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Version",
    )
    version_number = models.CharField(max_length=100, verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    is_version = models.BooleanField(verbose_name="Признак текущей версии")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
