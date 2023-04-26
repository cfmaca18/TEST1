from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.perfil import *


class PerfilViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer