from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.entrega import *


class EntregaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put