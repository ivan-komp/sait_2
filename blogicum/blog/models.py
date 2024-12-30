from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from core.models import PublishedModel

User = get_user_model()


class PostQuertySet(models.QuerySet):
    def published(self):
        return self.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return PostQuertySet(self.model).published()


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(
        unique=True,
        help_text="Идентификатор страницы для URL; "
        "разрешены символы латиницы, цифры, дефис и подчёркивание.",
        verbose_name="Идентификатор",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Location(PublishedModel):
    name = models.CharField(max_length=256, verbose_name="Название места")

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(
        help_text="Если установить дату и время в будущем — "
        "можно делать отложенные публикации.",
        verbose_name="Дата и время публикации",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Местоположение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        related_name="posts",
    )
    published = PublishedPostManager()
    objects = models.Manager()

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
