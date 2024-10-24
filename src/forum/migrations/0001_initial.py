# Generated by Django 4.2.15 on 2024-10-24 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Conversation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        help_text="The maximum number of characters is 100.",
                        max_length=100,
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="The maximum number of characters is 11000.",
                        max_length=11000,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="forum/conversation/images"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        default="Unknown",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="The maximum number of characters is 8000.",
                        max_length=8000,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="forum/comments/images"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        default="Unknown",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "conversation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="forum.conversation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
