from django.db import models

from .autor import Autor


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    paginas = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return self.titulo
