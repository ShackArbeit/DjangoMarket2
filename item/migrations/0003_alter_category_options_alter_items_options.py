# Generated by Django 5.1 on 2024-10-05 10:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0002_alter_category_options_items"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ("name",), "verbose_name_plural": "產品種類"},
        ),
        migrations.AlterModelOptions(
            name="items",
            options={"verbose_name_plural": "產品項目"},
        ),
    ]
