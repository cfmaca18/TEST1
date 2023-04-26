from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.categoria import *


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put