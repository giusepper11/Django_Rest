from rest_framework.viewsets import ModelViewSet

from avaliacoes.api.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacoesViewSet(ModelViewSet):
    """
    Um viewset basico para observar e editar pontos turisticos
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
