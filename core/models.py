from django.db import models

from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from enderecos.models import Endereco


# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.nome

    @property
    def descricao_completa2(self):
        return '{} - {}'.format(self.nome, self.descricao)
