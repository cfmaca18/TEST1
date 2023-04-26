from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.centros_de_formacion import *


class Centros_de_formacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Centros_de_formacion.objects.all()
    serializer_class = Centros_de_formacionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put