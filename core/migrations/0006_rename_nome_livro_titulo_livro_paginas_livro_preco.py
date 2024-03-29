# Generated by Django 5.0.2 on 2024-03-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_livro_alter_autor_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="nome",
            new_name="titulo",
        ),
        migrations.AddField(
            model_name="livro",
            name="paginas",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
