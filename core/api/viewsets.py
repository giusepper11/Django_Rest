from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    Um viewset basico para observar e editar pontos turisticos
    """
    # Comentando ou removendo o queryset é necessario implementar um metodo get_queryset
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    lookup_field = 'nome'  # esta variavel q define a busca pela url, por padrao é a pk ou id, deve ser campo unique
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # tambem adicionar o model no base_name na rota

        return PontoTuristico.objects.filter(aprovado=True)

    def create(self, request, *args, **kwargs):
        # mantendo comportamento padrao
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # sobescrever a funcao de delete
        pass

    # action para detail
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None, **kwargs):
        return Response({'denunciado': pk})

    # action para endpoint
    @action(methods=['get'], detail=False)
    def test(self, request):
        pass
