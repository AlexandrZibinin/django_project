from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name="Slug")
    text = models.TextField(blank=True, null=True, verbose_name="Содержание")
    image = models.ImageField(upload_to="blog/photo", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateField(verbose_name="Дата создания")
    public = models.BooleanField(default=False ,verbose_name="Публикация")
    views = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
