from rest_framework.viewsets import ModelViewSet

from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecosViewSet(ModelViewSet):
    """
    Um viewset basico para observar e editar enderecos
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
