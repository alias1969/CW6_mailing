from django.db import models

from mailings.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        help_text="Введите заголовок",
        max_length=100,
    )
    content = models.TextField(
        verbose_name="Содержимое статьи",
        help_text="Введите содержимое",
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="blogs/",
        **NULLABLE,
        help_text="Загрузите скан статьи",
    )
    count_views = models.IntegerField(
        verbose_name="количество просмотров",
        default=0,
    )
    publication_at = models.DateField(
        verbose_name="Дата публикации",
        auto_now_add=True,
    )
    is_published = models.BooleanField(default=True,
        verbose_name="Опубликовано"
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ("title",)

    def __str__(self):
        return f"{self.title}"