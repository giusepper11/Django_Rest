from rest_framework.decorators import action
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

    def get_queryset(self):
        # tambem adicionar o model no base_name na rota
        return PontoTuristico.objects.filter(aprovado=True)

    def destroy(self, request, *args, **kwargs):
        # sobescrever a funcao de delete
        pass

    #action para detail
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None, **kwargs):
        return Response({'denunciado':pk})

    #action para endpoint
    @action(methods=['get'], detail=False)
    def test(self, request):
        pass