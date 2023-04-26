from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.equipo_trabajo import *


class Equipo_trabajoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipo_trabajo.objects.all()
    serializer_class = Equipo_trabajoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put