# Generated by Django 5.1.1 on 2024-09-20 18:35

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                (
                    "published",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 9, 20, 18, 35, 59, 52210, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="blog")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("categories", models.ManyToManyField(to="blog.category")),
            ],
            options={
                "verbose_name": "post",
                "verbose_name_plural": "posts",
                "ordering": ["-created"],
            },
        ),
    ]
