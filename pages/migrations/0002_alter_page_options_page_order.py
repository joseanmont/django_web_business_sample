# Generated by Django 5.1.1 on 2024-09-23 23:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={
                "ordering": ["order", "title"],
                "verbose_name": "page",
                "verbose_name_plural": "pages",
            },
        ),
        migrations.AddField(
            model_name="page",
            name="order",
            field=models.SmallIntegerField(default=0),
        ),
    ]
