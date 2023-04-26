from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.ficha import *


class FichaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put