from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.programa import *


class ProgramaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put