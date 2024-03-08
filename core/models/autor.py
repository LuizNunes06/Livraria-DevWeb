from django.db import models 

class Autor(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural="Autores"
        verbose_name="Autor"