# Generated by Django 5.0.2 on 2024-03-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Editora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("site", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="categoria",
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias"},
        ),
    ]