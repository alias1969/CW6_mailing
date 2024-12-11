# Generated by Django 5.1.1 on 2024-12-08 15:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_time",
                    models.DateTimeField(
                        auto_now=True, verbose_name="дата и время последней попытки"
                    ),
                ),
                ("status", models.BooleanField(verbose_name="статус попытки")),
                (
                    "server_response",
                    models.TextField(
                        blank=True, null=True, verbose_name="ответ почтового сервера"
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
                "ordering": ["date_time", "status"],
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите email", max_length=254, verbose_name="email"
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        help_text="ФИО", max_length=100, verbose_name="ФИО"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Введите комментарий",
                        null=True,
                        verbose_name="Комментарий",
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
                "ordering": ["email", "full_name"],
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_time",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        help_text="Выберите время отправки",
                        null=True,
                        verbose_name="Дата и время первой отправки рассылки",
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Day", "Раз в день"),
                            ("Week", "Раз в неделю"),
                            ("Month", "Раз в месяц"),
                        ],
                        help_text="Выберите периодичность отправки",
                        max_length=20,
                        null=True,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "создана"),
                            ("running", "запущена"),
                            ("completed", "завершена"),
                        ],
                        default="created",
                        max_length=20,
                        verbose_name="Статус рассылки",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ["date_time", "status"],
                "permissions": [
                    ("can_view_mailing", "Can view mailing"),
                    ("can_block_user", "Can block user"),
                    ("can_disable_mailing", "Can disable mailing"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "topic",
                    models.CharField(
                        blank=True,
                        help_text="Введите тему письма",
                        max_length=30,
                        null=True,
                        verbose_name="тема письма",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        blank=True,
                        help_text="Введите содержимое письма",
                        null=True,
                        verbose_name="тело письма",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ["topic"],
            },
        ),
    ]