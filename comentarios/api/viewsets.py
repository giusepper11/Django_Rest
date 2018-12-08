from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentariosSerializer
from comentarios.models import Comentario


class ComentariosViewSet(ModelViewSet):
    """
    Um viewset basico para observar e editar comentários
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer
