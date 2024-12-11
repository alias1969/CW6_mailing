from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

NULLABLE = {"null": True, "blank": True}

class User(AbstractUser):
    """Класс пользователей"""

    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Уникальное имя для обратного доступа
        blank=True,
        help_text="Группы пользователя. Пользователь получит права своих групп.",
        related_query_name="custom_user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Уникальное имя для обратного доступа
        blank=True,
        help_text="Права пользователя.",
        related_query_name="custom_user_permission",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
