from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.rol import *


class RolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put